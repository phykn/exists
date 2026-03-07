# How to Create a Python pip Library

A step-by-step guide to turning a simple function into an installable pip package,
using `exists` as a minimal working example.

## 1. Project Structure

```
my_package/
├── pyproject.toml       # Package config (required)
├── my_package/
│   ├── __init__.py      # Public API
│   └── core.py          # Implementation
├── README.md
└── LICENSE
```

The two essentials are **`pyproject.toml`** and the **package directory**.

## 2. `pyproject.toml`

### Minimal

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
```

| Field | Description |
|---|---|
| `[build-system]` | Build tool config. `requires` and `build-backend` must be set together |
| `name` | Package name used in `pip install <name>` |
| `version` | Package version |

### Optional fields

```toml
[project]
name        = "my_package"
version     = "0.1.0"
description = "One-line description"           # Shown in PyPI search
readme      = "README.md"                      # Displayed on PyPI page
license     = {text = "MIT"}
requires-python = ">=3.7"
dependencies    = ["numpy", "requests>=2.0"]
```

## 3. Package Code

### `__init__.py` — Public API

```python
from .core import exists
```

Users can then write `from my_package import exists` directly.

As the package grows, re-export from multiple files:

```python
from .core import exists
from .utils import helper_func
from .models import MyModel
```

### `core.py` — Implementation

```python
def exists(x: object) -> bool:
    """Check if a value is not None.

    Args:
        x: Value to check.

    Returns:
        True if x is not None, False otherwise.
    """
    return x is not None
```

## 4. Installation

| Command | When to use |
|---|---|
| `pip install .` | Production install. Code changes are **not** reflected after install |
| `pip install -e .` | Dev mode. Code changes are reflected immediately ✅ |

## 5. Building a `.whl` File

```bash
pip wheel . --no-deps -w dist/
```

A `.whl` file is created in `dist/`. Install it in another environment:

```bash
pip install my_package-0.1.0-py3-none-any.whl
```

## 6. Usage

```python
from exists import exists

exists(42)    # True
exists(None)  # False
exists(0)     # True  — 0 is not None
exists("")    # True  — "" is not None
```
