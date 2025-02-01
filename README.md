Ecco un **README.md** completo per `pyinit`, con istruzioni di installazione, utilizzo e funzionalità. 🚀  

---

### 📜 **README.md**
```markdown
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

