# Crypto Arbitrage Bot

This is a cryptocurrency arbitrage trading bot that monitors price differences between exchanges and executes trades when profitable opportunities are found.

## Features

- Real-time price monitoring across multiple exchanges
- Configurable trading pairs and profit thresholds
- Automated trade execution
- Error handling and logging
- Support for Binance and Coinbase exchanges (easily extensible)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example` and add your exchange API keys:
```bash
cp .env.example .env
```

3. Configure your trading parameters in `config.py`:
- Adjust the `MINIMUM_PROFIT_THRESHOLD`
- Modify the `TRADING_PAIRS` list
- Set your preferred `TRADE_AMOUNT`

## Usage

Run the bot:
```bash
python arbitrage_bot.py
```

## Safety Considerations

- Start with small trade amounts for testing
- Monitor the bot's performance closely
- Ensure you understand the risks involved
- Keep your API keys secure
- Test thoroughly in a sandbox environment first

## Disclaimer

Trading cryptocurrencies involves substantial risk of loss. This bot is for educational purposes only. Use at your own risk.
