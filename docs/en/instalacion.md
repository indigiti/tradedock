[← English documentation](README.md)

# Installing Trading Hub

The application is compiled locally from this repository and installed as `Trading Hub.app`.

## Requirements

| Requirement | Details |
|---|---|
| Mac | Apple Silicon, M1 or later, `arm64` architecture |
| macOS | Version 12 or later |
| Build SDK | .NET 10 SDK |
| Network | Internet access during the first build to restore NuGet packages |
| Claude Code | Optional, required only for Claude-assisted features |

Check your Mac:

```bash
uname -m
sw_vers -productVersion
```

The first command must report `arm64`. An Intel Mac is not supported by this build process. Once installed, the application is self-contained; end users do not need the .NET SDK.

## Option 1: Install using Claude Code

Install and log into Claude Code, open a terminal in the repository, run `claude`, and ask:

```text
Install Trading Hub by following CLAUDE.md. Check compatibility and prerequisites first.
```

Claude Code should check the architecture, set up the .NET SDK if necessary, build the application, and launch it. No brokerage passwords or API credentials are needed for installation. If an unrelated app named Trading Hub already exists in Applications, review the replacement before continuing.

## Option 2: Manual installation

```bash
git clone https://github.com/indigiti/tradedock.git
cd tradedock
~/.dotnet/dotnet --list-sdks
```

If .NET SDK 10 is absent, install it in your home directory:

```bash
curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/dotnet-install.sh
bash /tmp/dotnet-install.sh --channel 10.0
```

Then build and install:

```bash
./build-app.sh --install
open "/Applications/Trading Hub.app"
```

`build-app.sh` adds `~/.dotnet` to its own PATH, publishes a Release `osx-arm64` self-contained build, assembles and signs the app, and writes a copy under `dist/Trading Hub.app`. With `--install`, it replaces the application in `/Applications`. Without that flag, it leaves Applications untouched.

### Code signing

Without a developer certificate, the script applies ad-hoc signing. An app copied to a different Mac may require **Right-click → Open** on first launch. If you have a signing certificate, create the git-ignored `build.local.env` file containing `SIGN_IDENTITY` and `BUNDLE_ID` according to the build script's documentation. Be sure the signing identity exists in your macOS keychain.

## Optional Claude Code integration

Trading Hub uses your existing Claude Code CLI and account, rather than a separate Claude API key. If necessary, make the command accessible:

```bash
command -v claude
claude --version
mkdir -p ~/.local/bin
ln -sf "$(command -v claude)" ~/.local/bin/claude
```

The `TRADINGHUB_CLAUDE_CLI` environment variable can select a specific CLI. Log in from Terminal with `claude` and `/login`. Without the CLI, charting, manual trading, data management, and backtesting remain available.

## Local files

| Location | Content |
|---|---|
| `~/Library/Application Support/Trading Hub` | Settings, public connection metadata, workspaces, ticks, history, drawings, templates, simulation/account records, backtests, and live strategy state |
| `~/Documents/Trading Hub/Estrategias` | User-written C# strategies and reports |
| `~/Documents/Trading Hub/Indicadores` | User-written C# indicators |
| macOS Keychain | Broker passwords, private API credentials, access tokens |

Important files inside Application Support include `settings.json`, `connections.json` (nonsecret metadata), `workspace.json`, `Ticks/`, `Klines/`, `Drawings/`, `Accounts/`, `Backtests/`, `Live/`, and `crash.log`.

## Updating

Completely quit the app using **Command-Q** or its menu-bar **Quit** action. Closing its window may leave it running in the menu bar. Then:

```bash
git pull
./build-app.sh --install
```

Your data and strategy folders are outside this repository and should be preserved.

## Uninstalling

Completely quit the app; remove `/Applications/Trading Hub.app`; remove any **Trading Hub** entries from Keychain Access; and, **only if you intentionally want to erase the data**, delete the corresponding Application Support and Documents folders. Deletion is irreversible.

## Troubleshooting

If the build fails, check that SDK 10 is installed and network access can restore NuGet packages. If the application crashes, check `crash.log` in its data directory. Do not use a production trading account as a test fixture.
