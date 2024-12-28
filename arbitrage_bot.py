import ccxt
import time
import logging
from datetime import datetime
from config import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ArbitrageBot:
    def __init__(self):
        self.exchanges = {
            'binance': ccxt.binance({
                'apiKey': BINANCE_API_KEY,
                'secret': BINANCE_SECRET_KEY,
                'enableRateLimit': True
            }),
            'coinbase': ccxt.coinbase({
                'apiKey': COINBASE_API_KEY,
                'secret': COINBASE_SECRET_KEY,
                'enableRateLimit': True
            })
        }
        
    def fetch_ticker(self, exchange, symbol):
        try:
            ticker = exchange.fetch_ticker(symbol)
            return {
                'bid': ticker['bid'],
                'ask': ticker['ask'],
                'exchange': exchange.id
            }
        except Exception as e:
            logger.error(f"Error fetching {symbol} price from {exchange.id}: {str(e)}")
            return None

    def calculate_profit_potential(self, buy_price, sell_price):
        profit_percentage = ((sell_price - buy_price) / buy_price) * 100
        return profit_percentage

    def execute_trade(self, buy_exchange, sell_exchange, symbol, amount):
        try:
            # Place buy order
            buy_order = buy_exchange.create_market_buy_order(symbol, amount)
            logger.info(f"Buy order placed on {buy_exchange.id}: {buy_order}")

            # Place sell order
            sell_order = sell_exchange.create_market_sell_order(symbol, amount)
            logger.info(f"Sell order placed on {sell_exchange.id}: {sell_order}")

            return True
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
            return False

    def monitor_opportunities(self):
        while True:
            for symbol in TRADING_PAIRS:
                prices = []
                
                # Fetch prices from all exchanges
                for exchange in self.exchanges.values():
                    ticker = self.fetch_ticker(exchange, symbol)
                    if ticker:
                        prices.append(ticker)

                if len(prices) < 2:
                    continue

                # Find best buy and sell prices
                best_buy = min(prices, key=lambda x: x['ask'])
                best_sell = max(prices, key=lambda x: x['bid'])

                profit_potential = self.calculate_profit_potential(
                    best_buy['ask'],
                    best_sell['bid']
                )

                if profit_potential > MINIMUM_PROFIT_THRESHOLD:
                    logger.info(f"Arbitrage opportunity found for {symbol}:")
                    logger.info(f"Buy from {best_buy['exchange']} at {best_buy['ask']}")
                    logger.info(f"Sell on {best_sell['exchange']} at {best_sell['bid']}")
                    logger.info(f"Potential profit: {profit_potential:.2f}%")

                    # Execute trade if profit is above threshold
                    if self.execute_trade(
                        self.exchanges[best_buy['exchange']],
                        self.exchanges[best_sell['exchange']],
                        symbol,
                        TRADE_AMOUNT
                    ):
                        logger.info("Trade executed successfully!")

            time.sleep(1)  # Wait for 1 second before next check

def main():
    bot = ArbitrageBot()
    logger.info("Starting arbitrage bot...")
    bot.monitor_opportunities()

if __name__ == "__main__":
    main()
