[← English documentation](README.md)

# Install with Claude Code

Use an Apple Silicon Mac running macOS 12 or later and a working Claude Code subscription. Open the repository folder in Terminal and run `claude`.

Ask:

```text
Install Trading Hub from this repository. Follow CLAUDE.md; inspect architecture, macOS version, and .NET SDK 10 first. Do not request any broker passwords or API tokens for installation. Build, install, verify the app, and report any errors.
```

The installer should check `uname -m` is `arm64`, install .NET SDK 10 under `~/.dotnet` if missing, execute `./build-app.sh --install`, verify the app under `/Applications/Trading Hub.app`, and open it.

Before replacing an existing app named Trading Hub that might be unrelated, the assistant should ask for approval. A simulated account is available on first launch. Add market-data connections only after reviewing their credentials and permissions.

To update later, completely quit Trading Hub, run `git pull` and `./build-app.sh --install` in the repository, and verify the installed version.

Troubleshoot by reading the **first actual compile or install error**, checking internet connectivity for NuGet restore, confirming SDK 10 is present, and reviewing the local `crash.log` if startup fails. Do not report a successful installation unless verified.
