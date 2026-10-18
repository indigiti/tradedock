[← English documentation](README.md)

# Privacy and security

Trading Hub runs locally on your Mac. The repository describes no Trading Hub-hosted telemetry, account service, or automatic crash upload. However, connected brokers, exchanges, and Claude Code do exchange information with their respective remote services.

## Stored locally

| Location | Contains |
|---|---|
| `~/Library/Application Support/Trading Hub` | Settings, nonsecret connection metadata, workspace, tick and candle history, drawings, templates, account records, backtests, live portfolios |
| `~/Documents/Trading Hub` | C# strategies, C# indicators, and generated reports |
| macOS Keychain | Passwords, API secrets, access tokens, Databento API key |

The application also keeps Claude chat history and some lab chart screenshots locally and records unexpected errors in `crash.log`. Secrets should not be written to project source files or bundled into bug reports.

## When data leaves the Mac

- Live market data/history connects to the configured broker or exchange.
- Actual broker account orders go to that broker; simulated orders remain local.
- Databento requests transmit your credential to Databento and paid downloads should be cost-confirmed.
- Claude Code interactions, accessible code files, strategy results, metrics, and selected screenshots may be transmitted to **Anthropic** through your Claude account. Anthropic's data policies apply.
- Browser links and provider OAuth authorization pages open only when requested.
- Package restore during builds downloads .NET/NuGet dependencies.

## Keychain

Passwords, tokens, and private keys live in macOS Keychain. `connections.json` retains public connection properties, such as usernames and public key IDs. Deleting a connection removes its associated stored secrets. The lab must never expose credentials to Claude or to test fixtures.

## Real trading controls

Real order capability is opt-in per connection. Confirmation preferences may be adjusted; verify all live risk limits before enabling execution. Automated real-account strategies do not automatically resume by default. A live risk agent's real-account allocation proposals require approval.

## Development safety

Unit tests and headless visual tests must run against temporary directories, including `TRADINGHUB_DATA_DIR`, `TRADINGHUB_STRATEGIES_DIR`, and `TRADINGHUB_INDICATORS_DIR`, plus a fake secrets store under `TRADINGHUB_KEYCHAIN_FILE`. Do not run two instances against the same live tick-data files.

## Removing your data

Completely quit the application; delete its Application Support directory and optional Documents directory only if you no longer need those assets; remove Trading Hub credentials from Keychain Access; and uninstall the app. Back up your strategies and recorded history first. Deletion cannot be undone.
