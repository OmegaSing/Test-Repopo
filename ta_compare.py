#!/usr/bin/env python3
"""Technical Analysis Comparison Script
Compares TA signals across multiple tickers.
Usage: Import and call compare_tickers(ticker_list)
"""

import json
import sys

# Cached TA data from OmegaClaw technical-analysis runs
TA_CACHE = {
    "IONQ": {"buy": 13, "sell": 0, "total": 13, "rsi": 68.08, "macd": 1.94, "adx": 24.06, "verdict": "STRONG BUY"},
    "MU": {"buy": 11, "sell": 2, "total": 13, "rsi": 59.8, "macd": 14.65, "adx": 18.1, "verdict": "STRONG BUY"},
    "SDGR": {"buy": 10, "sell": 3, "total": 13, "rsi": 50.9, "macd": -0.08, "adx": 13.9, "verdict": "MODERATE BUY"},
    "RGTI": {"buy": 0, "sell": 0, "total": 0, "rsi": 0, "macd": 0, "adx": 0, "verdict": "NO DATA"}
}

def compare_tickers(tickers=None):
    if tickers is None:
        tickers = list(TA_CACHE.keys())
    print(f"{'Ticker':<8} {'Buy/Total':<12} {'RSI':<8} {'MACD':<10} {'ADX':<8} {'Verdict'}")
    print("-" * 60)
    for t in tickers:
        d = TA_CACHE.get(t, {"buy": 0, "sell": 0, "total": 0, "rsi": 0, "macd": 0, "adx": 0, "verdict": "UNKNOWN"})
        print(f"{t:<8} {d['buy']}/{d['total']:<10} {d['rsi']:<8.1f} {d['macd']:<10.2f} {d['adx']:<8.1f} {d['verdict']}")
    # Rank by buy ratio
    ranked = sorted(tickers, key=lambda t: TA_CACHE.get(t, {}).get("buy", 0) / max(TA_CACHE.get(t, {}).get("total", 1), 1), reverse=True)
    print(f"\nRanking: {' > '.join(ranked)}")
    return ranked

if __name__ == "__main__":
    tickers = sys.argv[1:] if len(sys.argv) > 1 else None
    compare_tickers(tickers)
