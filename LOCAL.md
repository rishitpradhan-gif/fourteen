# Run Fourteen locally

Reproduce the sharp fourteen-ply fixed-pairing obstruction.

**[Download the ready-to-run ZIP](https://github.com/rishitpradhan-gif/fourteen/releases/download/local-v1/fourteen-local.zip)** · [All tools](https://github.com/rishitpradhan-gif/rishitpradhan-gif/blob/main/TOOLS.md)

## Three steps

1. Install Python 3.10+ if it is not already on your computer.
2. Download the ZIP above, **extract all files**, and open a terminal in the extracted folder (the one containing verify.py).
3. Run:

```sh
python3 verify.py
python3 attack.py
```

Read the printed verification results. This is a command-line research verifier, not a graphical app.

Python 3.10+. Uses only the Python standard library.

Keep the terminal open while using a server. Press **Ctrl+C** to stop it. Research verifiers exit after finishing their checks.

## If you get stuck

- **Windows:** replace `python3` with `py -3` in Python commands. If neither works, install Python from [python.org](https://www.python.org/downloads/). For the APIs, install Node from [nodejs.org](https://nodejs.org/en/download).
- **“File not found”:** extract the ZIP first, then change into the inner folder containing the launcher. Do not run from inside the ZIP viewer.
- **“Command not found”:** check `python3 --version` / `py -3 --version`, or `node --version` for the APIs. Reopen the terminal after installing a runtime.

The proofs are in `PROOFS.md`. A passing run checks the included finite instances; read the proofs for the general statements and their exact scope.

These downloads run locally. The local servers bind to your own computer; they are not configured as public multi-user services.
