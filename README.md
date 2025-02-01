# 🚀 PyInit - Inizializza Progetti Python in Secondi!

PyInit è un tool CLI che crea automaticamente la struttura di un progetto Python, configurando ambiente virtuale (`venv`) o **Poetry**, e opzionalmente un **Dockerfile**.

✅ **Crea una struttura ben organizzata**  
✅ **Supporta sia venv che Poetry**  
✅ **Log avanzati e barra di caricamento (con `rich`)**  
✅ **Funziona con `pipx` per installazione globale**  

---

## 📦 **Installazione**
### 1️⃣ **Con `pipx` (Raccomandato)**
```bash
pipx install pyinit
```
✅ Questo permette di usare `pyinit` ovunque senza inquinare il sistema.

### 2️⃣ **Con `pip`**
```bash
pip install pyinit
```

### 3️⃣ **Per Sviluppatori (Installazione Locale)**
Se vuoi modificare il codice:
```bash
git clone https://github.com/tuo-username/pyinit.git
cd pyinit
pipx install .
```

---

## 🚀 **Utilizzo**
### 1️⃣ **Creare un Nuovo Progetto Python**
```bash
pyinit mio_progetto
```
✔️ **Crea una cartella con la struttura base**  
✔️ **Genera un ambiente virtuale**  
✔️ **Installa `pytest` e `black`**  

### 2️⃣ **Usare Poetry invece di venv**
```bash
pyinit mio_progetto --poetry
```
✔️ **Inizializza Poetry e aggiunge le dipendenze**  
✔️ **Usa `pipx run poetry` se Poetry non è installato globalmente**  

### 3️⃣ **Aggiungere un Dockerfile**
```bash
pyinit mio_progetto --docker
```
✔️ **Genera un `Dockerfile` pronto all'uso!**  

### 4️⃣ **Usare Tutte le Opzioni**
```bash
pyinit mio_progetto --poetry --docker
```
✔️ **Progetto con Poetry e Dockerfile in un solo comando!**  

---

## 📂 **Struttura del Progetto**
Dopo aver eseguito `pyinit`, troverai:

```
mio_progetto/
│── venv/              # Ambiente virtuale (se non usi Poetry)
│── src/               # Codice sorgente
│   ├── __init__.py
│   ├── main.py        # File principale
│── tests/             # Cartella per i test
│   ├── __init__.py
│── docs/              # Documentazione
│── .gitignore
│── .env
│── requirements.txt   # Dipendenze
│── Makefile           # Comandi utili
│── setup.py           # Configurazione pacchetto
│── Dockerfile         # (opzionale)
│── README.md
```

---

## 🔥 **Esempio di Output**
Quando esegui `pyinit`, vedrai un output chiaro e interattivo:

```bash
🚀 Creazione del progetto `mio_progetto` in corso...
📂 Creazione struttura progetto... [██████████] 100%
🐍 Creazione dell'ambiente virtuale...
📦 Installazione dipendenze... [██████████] 100%
✅ Progetto `mio_progetto` creato con successo!
```

---

## 🛠 **Gestione Manuale**
Se non vuoi usare `pyinit`, puoi replicare i passi manualmente:

1. **Crea la cartella e un ambiente virtuale**
   ```bash
   mkdir mio_progetto && cd mio_progetto
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel pytest black
   ```
2. **Crea la struttura**
   ```bash
   mkdir src tests docs
   touch src/__init__.py src/main.py tests/__init__.py .gitignore .env requirements.txt README.md
   ```
3. **(Opzionale) Inizializza Poetry**
   ```bash
   poetry init -n
   poetry add pytest black
   ```

---

## ❓ **FAQ**
### 🔹 **`rich` è obbligatorio?**
No, `pyinit` funziona anche senza `rich`, ma i log saranno meno leggibili.

Se vuoi i log colorati, installalo con:
```bash
pipx inject pyinit rich
```

### 🔹 **Come aggiorno `pyinit`?**
Se lo hai installato con `pipx`, esegui:
```bash
pipx upgrade pyinit
```

Se usi `pip`:
```bash
pip install --upgrade pyinit
```

### 🔹 **Posso rimuoverlo?**
Sì! Con:
```bash
pipx uninstall pyinit  # Se usi pipx
pip uninstall pyinit   # Se usi pip
```

---

## 📌 **Contribuire**
Vuoi migliorare `pyinit`? Sentiti libero di **contribuire** aprendo una **pull request** o segnalando un problema su [GitHub](https://github.com/tuo-username/pyinit/issues).

---

## 🏆 **Licenza**
Distribuito sotto licenza **MIT**.  
Creazione di **[Il Tuo Nome]**, ispirato alla necessità di velocizzare la configurazione dei progetti Python. 🚀
Here's the **English version** of the `README.md`, now updated with the improved `.gitignore`. 🚀  

---

### 📜 **README.md**
```markdown
# 🚀 PyInit - Instantly Set Up a Python Project!

**PyInit** is a CLI tool that automates the creation of a structured Python project, configuring a **virtual environment (`venv`)** or **Poetry**, and optionally adding a **Dockerfile**.

✅ **Generates a structured Python project**  
✅ **Supports both `venv` and Poetry**  
✅ **Advanced logs and a progress bar (with `rich`)**  
✅ **Works with `pipx` for global installation**  

---

## 📦 **Installation**
### 1️⃣ **With `pipx` (Recommended)**
```bash
pipx install pyinit
```
✅ This allows using `pyinit` globally without polluting the system.

### 2️⃣ **With `pip`**
```bash
pip install pyinit
```

### 3️⃣ **For Developers (Local Installation)**
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

## 📌 **Contributing**
Want to improve **PyInit**? Feel free to **contribute** by opening a **pull request** or reporting an issue on [GitHub](https://github.com/your-username/pyinit/issues).

---

## 🏆 **License**
Distributed under the **MIT License**.  
Created by **[Your Name]**, inspired by the need to streamline Python project setup. 🚀
