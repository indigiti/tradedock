[← English documentation](README.md)

# Development guide

Trading Hub is a C#/.NET 10 and Avalonia application using SkiaSharp for chart rendering. The solution is `TradingHub.slnx`.

## Source organization

| Project | Responsibilities |
|---|---|
| `TradingHub.Core` | Market instruments, data, provider feeds, orders, and account abstractions |
| `TradingHub.Sdk` | Indicator API and compatible SDK features |
| `TradingHub.Charting` | Chart models, controllers, DOM/footprint, drawing, and rendering |
| `TradingHub.Indicators.Native` | Native studies |
| `TradingHub.Indicators.Technical` | Technical indicator compatibility |
| `TradingHub.Scripting` | C# strategy and indicator compilation |
| `TradingHub.Strategies` | Backtesting, optimization, portfolio analysis, live strategy runner |
| `TradingHub.App` | Avalonia windows, views, settings, services, and Claude integration |
| `TradingHub.Tests` | Unit, provider, strategy, optimization, data-integrity, and regression tests |

## Build and test

```bash
export PATH="$HOME/.dotnet:$PATH"
dotnet build TradingHub.slnx
dotnet test tests/TradingHub.Tests
```

The .NET 10 SDK and compatible workloads/packages must be installed. The macOS distributable build is produced with `./build-app.sh`.

## Headless visual scenes

The repository contains `tools/TradingHub.UiSnapshot` for deterministic, offscreen scenes. Example:

```bash
dotnet run --project tools/TradingHub.UiSnapshot -- /tmp/tradinghub-snapshots 4 trading conexiones panel footprint mercado
```

Do not point these tools at actual production data. Verify their accepted arguments in `tools/TradingHub.UiSnapshot/Program.cs` before changing scene tests.

## Safe environment variables

`TRADINGHUB_DATA_DIR`, `TRADINGHUB_STRATEGIES_DIR`, and `TRADINGHUB_INDICATORS_DIR` redirect data to temporary fixtures. `TRADINGHUB_KEYCHAIN_FILE` can point to a fake secret store for tests. Actual broker passwords/tokens must never be embedded in test fixtures or commits.

## Adding a provider

Define a feed adapter behind the existing provider interfaces, distinguish history and live availability, and implement reconnect/rate-limit handling. Respect market sessions, tick size, currency, provider entitlements, broker safety rules, and the existing user data layout. Add fake-provider regression tests before enabling any live order path.

## Adding studies or laboratory tools

Build indicators with the supported SDK lifecycle; expose parameters and render without blocking the UI. Claude/MCP tools must be scoped, auditable, and unable to exfiltrate production secrets.

## Validation and release process

For each change, check requirements, static/built output, tests, UI screenshot comparisons, provider error handling, chart loading, order routing, account safety, historical integrity, and backward compatibility. Treat any unexecuted check as **not verified**, never as passed.

For localization, specifically validate keyboard shortcuts, bindings, window size, dynamic text interpolation, source-code string integrity, test snapshots, and fallback to the original Spanish labels.
