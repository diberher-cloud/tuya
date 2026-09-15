"""Command-line interface for pulling TradingView market data.

Usage:
    python -m tvconnect.cli AAPL MSFT --exchange NASDAQ --screener america --interval 1d
"""

import argparse
import json
import sys

from .client import TradingViewClient, TradingViewError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch market data from TradingView.")
    parser.add_argument("symbols", nargs="+", help="Ticker symbols, e.g. AAPL BTCUSDT")
    parser.add_argument("--exchange", default="NASDAQ", help="Exchange, e.g. NASDAQ, BINANCE (default: NASDAQ)")
    parser.add_argument("--screener", default="america", help="Screener, e.g. america, crypto, forex (default: america)")
    parser.add_argument("--interval", default="1d", help="Interval: 1m,5m,15m,30m,1h,2h,4h,1d,1w,1mo (default: 1d)")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    client = TradingViewClient(screener=args.screener, exchange=args.exchange, interval=args.interval)

    results = []
    had_error = False
    for symbol in args.symbols:
        try:
            quote = client.get_quote(symbol)
            results.append(quote.to_dict())
        except TradingViewError as exc:
            had_error = True
            results.append({"symbol": symbol, "error": str(exc)})

    print(json.dumps(results, indent=2))
    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
