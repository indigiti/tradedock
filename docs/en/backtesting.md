[← English documentation](README.md)

# Backtesting, optimization, and validation

Backtesting replays market history through a C# strategy to estimate how it would have behaved under a set of execution assumptions. It is not a prediction of future returns.

## Historical data selection

Choose a compiled strategy, symbol, timeframe, testing period, and market-data source. Where applicable, choose Rithmic only, Databento only, or combined history. Tick-quality data supports more realistic order simulations than candle-only aggregates.

## Execution and costs

Backtest settings should include realistic fees, commissions, slippage, limit-order execution assumptions, position size, and broker-like order restrictions. The simulator models trade-level events and queue behavior where data allows. If a strategy relies on intrabar ordering, test whether the supplied history is granular enough.

## Results

Inspect net result, trade count, expectancy, win rate, profit factor, maximum drawdown, Sharpe-style statistics, equity progression, distributions, and trade-level outcomes. Compare results by market regime (trend/range and volatility) instead of relying on a single aggregate.

## Monte Carlo

Resample or otherwise perturb eligible trade outcomes to assess the variability of backtest performance. A strategy with large risk dispersion, unstable results, or very few independent trades needs further evidence.

## Parameter optimization

The application includes Bayesian/TPE optimization rather than only exhaustive grid searches. Timeframe may be an additional search parameter. Avoid selecting the single most profitable, fragile setting; examine neighboring regions and robust parameter plateaus.

## Walk-forward validation

Partition history into optimization and out-of-sample evaluation windows. Repeatedly optimize on training periods, then test held-out periods. Report combined out-of-sample behavior separately from training results.

## Overfitting controls

The strategy library includes diagnostics such as **PBO/CSCV**, **CPCV with embargo**, and **Deflated Sharpe Ratio**. Use these to investigate selection bias and overlapping training/test windows. The presence of these metrics does not make an overfit strategy reliable.

## Portfolios and reports

Combine backtests for multiple strategies to study cross-strategy dependence, correlations, portfolio drawdowns, and capital allocation. Keep the tested configuration, data-source choice, time intervals, and report artifacts so that results can be reproduced.

## Practical release gate

Require stable out-of-sample performance, sufficiently many independent trades, credible data coverage, realistic costs and fill behavior, acceptable drawdowns, parameter sensitivity review, and simulated live verification. Reject deployment if material gaps remain unresolved.
