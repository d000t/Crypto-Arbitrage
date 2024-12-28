import os
from dotenv import load_dotenv

load_dotenv()

# Exchange API credentials
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')
COINBASE_API_KEY = os.getenv('COINBASE_API_KEY')
COINBASE_SECRET_KEY = os.getenv('COINBASE_SECRET_KEY')

# Trading parameters
MINIMUM_PROFIT_THRESHOLD = 0.5  # Minimum profit percentage to execute trade
TRADING_PAIRS = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']  # Trading pairs to monitor
TRADE_AMOUNT = 100  # Amount in USDT to trade
MAX_TRADE_SLIPPAGE = 0.1  # Maximum allowed slippage percentage
