# Copilot Instructions for AI Coding Agents

## Project Overview
This repository contains a collection of Python scripts for learning and experimenting with basic programming concepts. The codebase is organized for educational purposes, with each file demonstrating a specific topic or feature in Python.

## Directory Structure
- `python/` — Main source directory. Each file covers a distinct concept:
  - `conditional.py`, `loop.py`, `whileloop.py` — Control flow examples
  - `dictionary.py`, `list.py`, `string.py` — Data structures and manipulation
  - `function.py` — Function definitions and usage
  - `input.py`, `typecasting.py` — User input and type conversion
  - `ques.py`, `ques1.py`, `ques3.py` — Practice questions and exercises
  - `hello.py` — Basic output
  - `__pycache__/` — Compiled Python files (ignore for code changes)
- `show.sh` — Shell script (purpose not documented; inspect before use)
- `README.md` — Minimal documentation; codebase is self-explanatory

## Developer Workflows
- **Run scripts:**
  - Use `python3 python/<filename>.py` to execute any script.
  - No build system or dependency management is present; scripts are standalone.
- **Debugging:**
  - Directly edit and run scripts. No integrated debugging tools or configuration files.
- **Testing:**
  - No formal test suite. Practice questions (`ques*.py`) may be used for manual validation.

## Conventions & Patterns
- Each Python file is self-contained and does not import from others.
- Naming is descriptive of the concept demonstrated (e.g., `loop.py` for loops).
- No external dependencies; only standard Python features are used.
- No classes or advanced OOP patterns; focus is on basic procedural code.
- Scripts are intended for direct execution, not as modules.

## Integration Points
- No external APIs, databases, or services are integrated.
- No cross-component communication; files do not interact with each other.

## Example Usage
```bash
python3 python/function.py
python3 python/loop.py
```

## Recommendations for AI Agents
- When adding new examples, follow the naming and organizational pattern in `python/`.
- Keep scripts simple and focused on a single concept.
- Update this file if new conventions or workflows are introduced.

---
For questions or unclear conventions, ask the user for clarification or examples.
