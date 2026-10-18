[← English documentation](README.md)

# Claude Code integration

Trading Hub invokes a locally installed **Claude Code CLI** using your own Claude session. It does not require entering a separate Claude API key in Trading Hub.

## Finding and logging into Claude Code

Check `claude --version` in Terminal. The application looks in common home-directory locations, the shell PATH, and compatible desktop installation locations. `TRADINGHUB_CLAUDE_CLI` can specify a binary. If not logged in, run `claude` and use `/login`.

## Model and permissions

The UI can configure compatible Claude model and effort preferences. Follow the permissions displayed for any agent session. Strategy work should be scoped to known project files and authorized tools. Never insert broker secrets into chat messages or source code.

## Strategy assistant

Under **Backtesting → Claude**, describe a C# strategy or request an existing strategy to be reviewed. The assistant can draft code, identify compile errors, propose corrections, and discuss results. Read its output as suggested source changes, not independently validated execution instructions.

## Laboratory

The in-app MCP laboratory exposes approved operations to let Claude run backtests, optimization, and walk-forward analysis, then produce reports. Work should be confined to dedicated data folders and the strategy/indicator workspace, with production accounts protected from test activity.

## Reports and evidence

Report outputs can include trade counts, statistics, equity curves, regime breakdowns, robustness diagnostics, and optimization parameters. Keep enough experiment metadata to reproduce each claim. Treat incomplete runs as failures, not as successful backtests.

## Data sent to Anthropic

Messages, strategy source files, indicators, permitted tool responses, backtest metrics, and selected chart screenshots may be sent to Anthropic under your Claude account. A portfolio risk agent can receive portfolio numbers and return proposals. See [Privacy](privacidad.md).

## Safe workflow

Request a change → review the diff → compile → run tests on temporary data → backtest → compare with baseline → simulate live behavior → authorize actual trading only after risk checks. An AI-generated strategy must not automatically bypass that process.
