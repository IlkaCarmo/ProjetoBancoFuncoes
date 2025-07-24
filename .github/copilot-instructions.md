# Copilot Instructions for ProjetoBancoFuncoes

## Project Overview
This is a simple Python project for a banking system challenge, implemented in a single script: `DesafioComFuncoesBanco.py`. The script simulates basic banking operations such as deposit, withdrawal, and statement viewing, using a command-line menu interface.

## Key File
- `DesafioComFuncoesBanco.py`: Contains all logic for user interaction, account balance, transaction limits, and operation history.

## Architecture & Data Flow
- All state (balance, limit, statement, withdrawal count) is managed via global variables at the top of the script.
- User actions are handled in a loop, responding to menu input.
- Functions are (or should be) used for each operation (e.g., deposit, withdraw, print statement), though the code may be partially implemented.

## Developer Workflow
- **Run the project:** Execute the script directly with Python 3:  
  `python DesafioComFuncoesBanco.py`
- **No build or test automation** is present. Manual testing is done by running the script and interacting via the menu.
- **No external dependencies** are required; only the Python standard library is used.

## Project-Specific Patterns
- Use clear, descriptive function names for each banking operation (e.g., `depositar`, `sacar`, `exibir_extrato`).
- Maintain all user-facing strings and menu prompts in Portuguese.
- Track the number of withdrawals and enforce a daily limit (`LIMITE_SAQUES`).
- The statement (`extrato`) is a string that accumulates transaction logs.
- All monetary values are handled as floats (representing BRL).

## Conventions
- All logic is in a single file; do not split into modules unless requirements change.
- Follow the existing variable naming and language conventions (Portuguese for variables and prompts).
- Keep the user interface simple and text-based.

## Example Pattern
```python
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def sacar(...):
    # lógica de saque

def depositar(...):
    # lógica de depósito
```

## When Extending
- Add new features as additional functions in the same file.
- Update the menu prompt and main loop to include new operations.
- Ensure all new prompts and comments remain in Portuguese.

---

For questions about project structure or workflow, review `DesafioComFuncoesBanco.py` as the single source of truth.
