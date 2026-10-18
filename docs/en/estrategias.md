[← English documentation](README.md)

# C# strategies

Trading Hub strategies are C# source files compiled through the built-in Roslyn editor. User strategies are stored separately from the application, typically under `~/Documents/Trading Hub/Estrategias`.

## Strategy lifecycle

Select or create a strategy under **Backtesting → Code**. Public configuration properties can provide adjustable parameters, including optimizable ranges. The strategy receives events and market-bar context according to its API contract. Use the project's existing examples to understand initialization, price access, open position state, order submission, and cleanup.

## Strategy parameters and market data

Typical inputs include instrument, timeframe, indicator lengths, entry filters, trading hours, maximum open positions, and stop/target distances. API facilities expose candle OHLCV and market context, as well as supported indicator series.

## Entries and exits

The strategy interface includes methods such as `EnterLong()`, plus configurable properties such as `StopLossTicks`. Use the actual current SDK signatures from the source code, not pseudocode copied from an external platform. Define risk constraints explicitly, and never assume a market, limit, or stop order will fill immediately.

## Automatic protection

Stops, targets, and trailing exits must respect tick size, side, and available position size. Bracket/OCO behavior should close or reduce an existing position without unintentionally reversing it. Always test partial fills and cancellation paths.

## Indicators and drawings

Strategies can reference included or custom C# indicators and create drawings or marks to explain decisions on charts. Ensure calculations use only data available at the relevant decision timestamp; avoid look-ahead bias and historical recalculation errors.

## Time and regime filters

Limit strategies to specified trading sessions and, where appropriate, market states such as trending/ranging or low/high volatility. Keep broker/exchange session calendars and daylight-saving changes in mind.

## Example workflows

1. **Moving-average crossover:** initialize fast and slow averages; trade only on permitted sessions; require a validated crossing; attach a defined stop and take-profit.
2. **Opening-range breakout:** define the opening range from completed bars; wait until its window closes; enter only after price clears the boundary; cap daily entries and losses.

These describe test setups, not guaranteed profitable strategies.

## Claude Code assistant

The Backtesting Claude assistant can draft a strategy, correct compiler errors, and evaluate historical results through the laboratory. Verify every proposed parameter and rule before compiling or launching an automated strategy.

## Before live deployment

Check compilation, deterministic backtests, data integrity, fill/commission assumptions, out-of-sample stability, risk limits, broker availability, account permissions, and safe stop/cancel handling. Begin with simulation.
