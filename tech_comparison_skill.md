# Technical Analysis Comparison Skill v1
## Purpose: Compare two tickers pre-earnings for relative positioning
## Inputs: ticker1, ticker2
## Process:
1. Run technical-analysis on both tickers
2. Compare RSI levels - higher RSI = more overbought = higher sell-the-news risk
3. Compare WILLR levels - closer to 0 = more overbought
4. Compare ADX - higher = stronger trend = momentum may persist
5. Compare MACD acceleration
6. Use MeTTa NAL to model contagion if same sector
## Output: Relative risk assessment and hedge recommendation
## Example applied: IONQ vs RGTI 2026-04-20
- IONQ RSI 68 vs RGTI RSI 62 -> IONQ more overbought
- IONQ WILLR -2.88 vs RGTI -4.71 -> IONQ more extreme
- Both ADX ~24 similar trend strength
- Conclusion: IONQ is hedge candidate, RGTI hold
## TODO: Automate with shell script calling technical-analysis twice
