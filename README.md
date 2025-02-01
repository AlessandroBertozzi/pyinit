# 🚀 PyInit

**PyInit** is a CLI tool that automates the creation of a structured Python project, configuring a **virtual environment (`venv`)** or **Poetry**, and optionally adding a **Dockerfile**.

✅ **Generates a structured Python project**  
✅ **Supports both `venv` and Poetry**  
✅ **Advanced logs and a progress bar (with `rich`)**  
✅ **Works with `pipx` for global installation**  

---

## 📦 **Installation**
### 1️⃣ **With `pipx` (Recommended)**
```bash
pipx install git+https://github.com/AlessandroBertozzi/pyinit.git
```
✅ Thi️s allows using `pyinit` globally without polluting the system.

### 2️⃣️ For Developers (Local Installation)**
If you want to modify the code:
```bash
git clone https://github.com/your-username/pyinit.git
cd pyinit
pipx install .
```

---

## 🚀 **Usage**
### 1️⃣ **Create a New Python Project**
```bash
pyinit my_project
```
✔️ **Creates a structured project folder**  
✔️ **Generates a virtual environment**  
✔️ **Installs `pytest` and `black`**  

### 2️⃣ **Use Poetry Instead of venv**
```bash
pyinit my_project --poetry
```
✔️ **Initializes Poetry and adds dependencies**  
✔️ **Uses `pipx run poetry` if Poetry isn't globally installed**  

### 3️⃣ **Add a Dockerfile**
```bash
pyinit my_project --docker
```
✔️ **Generates a ready-to-use `Dockerfile`**  

### 4️⃣ **Use All Options**
```bash
pyinit my_project --poetry --docker
```
✔️ **Creates a fully configured project with Poetry and Docker!**  

---

## 📂 **Project Structure**
After running `pyinit`, your project will be structured as follows:

```
my_project/
│── venv/              # Virtual environment (if not using Poetry)
│── src/               # Source code
│   ├── __init__.py
│   ├── main.py        # Main script
│── tests/             # Unit tests
│   ├── __init__.py
│── docs/              # Documentation
│── .gitignore
│── .env
│── requirements.txt   # Dependencies
│── Makefile           # Utility commands
│── setup.py           # Package configuration
│── Dockerfile         # (optional)
│── README.md
```

---

## 🔥 **Example Output**
When you run `pyinit`, you'll see clear, interactive output:

```bash
🚀 Creating project `my_project`...
📂 Generating project structure... [██████████] 100%
🐍 Setting up virtual environment...
📦 Installing dependencies... [██████████] 100%
✅ Project `my_project` successfully created!
```

---

## 📌 **Generated `.gitignore`**
PyInit includes a pre-configured `.gitignore` file for Python projects:

```plaintext
# 🔥 Python .gitignore - Generated by PyInit

# Virtual Environments
venv/
.venv/
env/
pip-log.txt
pip-delete-this-directory.txt

# Bytecode files
__pycache__/
*.py[cod]

# Logs & Debugging
*.log
*.out
*.err

# IDE Configurations
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# macOS
.DS_Store

# Jupyter Notebook Checkpoints
.ipynb_checkpoints/

# MyPy Type Checking
.mypy_cache/

# PyTest Cache
.pytest_cache/

# Coverage Reports
htmlcov/
.coverage
.tox/

# Build Artifacts
build/
dist/
*.egg-info/
```

---

## 🛠 **Manual Setup (Without PyInit)**
If you don't want to use `pyinit`, you can manually replicate the steps:

1. **Create a project folder and a virtual environment**
   ```bash
   mkdir my_project && cd my_project
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel pytest black
   ```
2. **Set up the folder structure**
   ```bash
   mkdir src tests docs
   touch src/__init__.py src/main.py tests/__init__.py .gitignore .env requirements.txt README.md
   ```
3. **(Optional) Initialize Poetry**
   ```bash
   poetry init -n
   poetry add pytest black
   ```

---

## ❓ **FAQ**
### 🔹 **Is `rich` required?**
No, `pyinit` works even without `rich`, but logs will be less readable.

If you want colored logs, install it with:
```bash
pipx inject pyinit rich
```

### 🔹 **How do I update `pyinit`?**
If installed with `pipx`:
```bash
pipx upgrade pyinit
```

If installed with `pip`:
```bash
pip install --upgrade pyinit
```

### 🔹 **How do I uninstall `pyinit`?**
```bash
pipx uninstall pyinit  # If installed with pipx
pip uninstall pyinit   # If installed with pip
```

---

## 🏆 **License**
Distributed under the **MIT License**.  
Created by **[Your Name]**, inspired by the need to streamline Python project setup. 🚀
