# How to Create a Python pip Library

A step-by-step example of turning a simple `exists` function into an installable pip package.

---

## 1. Project Structure

```
my_package/
├── pyproject.toml          # Package config (required)
├── my_package/
│   ├── __init__.py         # Package entry point
│   └── core.py             # Function implementation
├── README.md               # Optional
└── LICENSE                 # Optional
```

The two essentials are **`pyproject.toml`** and the **package directory**.

---

## 2. pyproject.toml (Minimal)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
```

### Required Fields

| Field | Description |
|---|---|
| `[build-system]` | Specifies the build tool. `requires` and `build-backend` must be paired together |
| `name` | Package name. Used in `pip install <name>` |
| `version` | Package version |

### Optional Fields (add as needed)

```toml
[project]
name = "my_package"
version = "0.1.0"
description = "One-line description"              # Shown in PyPI search
readme = "README.md"                              # Displayed on PyPI detail page
license = {text = "MIT"}                          # License
requires-python = ">=3.7"                         # Python version constraint
dependencies = ["numpy", "requests>=2.0"]         # Dependencies
```

---

## 3. Writing Package Code

### `__init__.py` — Keep it minimal

```python
from .core import exists
```

This allows users to write `from my_package import exists` directly.

### `core.py` — Actual implementation

```python
def exists(x):
    return x is not None
```

As functions grow, split into multiple files and re-export from `__init__.py`:

```python
# __init__.py
from .core import exists
from .utils import helper_func
from .models import MyModel
```

---

## 4. Installation

### Standard install

```bash
pip install .
```

Copies the project into site-packages. Code changes are **not** reflected after install.

### Development mode (recommended)

```bash
pip install -e .
```

Code changes are reflected immediately. Use this during development.

---

## 5. Building a .whl File

```bash
pip wheel . --no-deps -w dist/
```

A `.whl` file will be created in the `dist/` folder.

Install from the `.whl` file on another environment:

```bash
pip install my_package-0.1.0-py3-none-any.whl
```

---

## 6. Usage

```python
from exists import exists

exists(42)      # True
exists(None)    # False
exists(0)       # True  (0 is not None)
exists("")      # True  ("" is not None)
```
