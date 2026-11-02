# tuya

Python client for pulling live market data and technical analysis from
TradingView. It talks to TradingView's public scanner API directly — no
account, API key, or browser automation required.

## Install

```bash
pip install -r requirements.txt
```

## Usage

### CLI

```bash
python -m tvconnect.cli AAPL MSFT --exchange NASDAQ --screener america --interval 1d
```

Options:

- `--exchange` — e.g. `NASDAQ`, `NYSE`, `BINANCE` (default: `NASDAQ`)
- `--screener` — e.g. `america`, `crypto`, `forex` (default: `america`)
- `--interval` — one of `1m,5m,15m,30m,1h,2h,4h,1d,1w,1mo` (default: `1d`)

Output is a JSON array with price, recommendation, and indicator summaries
per symbol.

### Library

```python
from tvconnect import TradingViewClient

client = TradingViewClient(exchange="NASDAQ", screener="america", interval="1d")
quote = client.get_quote("AAPL")

print(quote.price, quote.recommendation)
print(quote.to_dict())
```

For other markets, pass the matching exchange/screener, e.g.:

```python
client = TradingViewClient(exchange="BINANCE", screener="crypto", interval="1h")
quote = client.get_quote("BTCUSDT")
```

## Requirements

Outbound HTTPS access to `scanner.tradingview.com` is required at runtime.

## Tests

```bash
pip install pytest
pytest
```

Tests mock the TradingView API call, so they run offline.

## Staff ejecutivo de agentes

Este repo incluye un equipo de subagentes de Claude Code (CEO, CFO, CTO, CRO, CCO,
General Counsel, CISO, COO, CMO, CPO, CHRO) y el comando `/comite-ejecutivo`.
Ver [docs/staff-ejecutivo.md](docs/staff-ejecutivo.md).
