# **Setting Up VS Code for AEs**  

## 🚀 **Setup Instructions (New Virtual Environment)**  

This guide walks you through setting up a fresh Python virtual environment with JupyterLab in **VS Code** while ensuring **seamless authentication**, **consistent formatting**, and **a unified workflow** for both **local development and customer deployment**.

By following these steps, you will:  
✅ **Avoid managing multiple credential files** – Use a single `credentials.json` file to switch between customers.  
✅ **Easily transition from local development to customer deployment** – Minimal modifications required.  
✅ **Stay within VS Code** – Leverage **GitHub Copilot**, keep a **single repository** for all customer work, and streamline collaboration.  
✅ **Ensure reproducibility** – Every project will have the same environment setup across machines.  

---

## 🔹 Prerequisites

Before proceeding, ensure you have:

✅ **Python 3.11+ installed** ([Download Python](https://www.python.org/downloads/))  
✅ **Git installed** ([Download Git](https://git-scm.com/downloads))  
✅ **VS Code installed** ([Download VS Code](https://code.visualstudio.com/))  

If you haven't installed these yet, follow the links above before continuing.


## **1️⃣ Fork the Repository**  

To maintain your own copy of the repository while still receiving updates from the original project, follow these steps:

1. **Go to GitHub** and fork the repository:  
   - Navigate to **[https://www.github.com/ChristopherHarp/SDL_Local_Setup](https://github.com/ChristopherHarp/SDL_Local_Setup)**  
   - Click **Fork** (this creates a copy in your GitHub account).  
2. **Clone your forked repository** in VS Code:  
   - Open the **Command Palette** (`Ctrl + Shift + P` on Windows/Linux, `Cmd + Shift + P` on Mac).  
   - Type **"Git: Clone"** and select it.  
   - Enter your forked repository URL:
     ```
     https://github.com/YOUR_GITHUB_USERNAME/sdl-local-setup.git
     ```
   - Select a location on your machine and open it in VS Code.
3. **Alternatively, use the terminal:**
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/sdl-local-setup.git
   cd sdl-local-setup
   code .
   ```
4. **Set up the original repo as an upstream remote**:
   ```sh
   git remote add upstream https://github.com/seeq12/sdl-local-setup.git
   ```
5. **Verify your remotes**:
   ```sh
   git remote -v
   ```
   You should see:
   ```
   origin    https://github.com/YOUR_GITHUB_USERNAME/sdl-local-setup.git (fetch)
   origin    https://github.com/YOUR_GITHUB_USERNAME/sdl-local-setup.git (push)
   upstream  https://github.com/seeq12/sdl-local-setup.git (fetch)
   upstream  https://github.com/seeq12/sdl-local-setup.git (push)
   ```

### 🔹 Suggestion: Explain Why Upstream is Needed  
**Why set up `upstream`?**  
The original repository (`upstream`) may receive bug fixes, new features, or dependency updates.  
By setting `upstream`, you can pull the latest changes while keeping your modifications intact.  

### 🔹 Suggestion: Reminder to Keep Fork Updated  
Since your fork is separate from the original repo, you’ll need to **fetch and merge updates periodically**:

1. **Fetch the latest changes from upstream**:
   ```sh
   git fetch upstream
   ```
2. **Merge changes into your local branch**:
   ```sh
   git merge upstream/main
   ```
3. **Push the updates to your fork**:
   ```sh
   git push origin main
   ```

🚀 **Now, your fork stays up to date with the original repository while keeping your modifications!**

---

## **2️⃣ Install Required VS Code Extensions**  

Before setting up the virtual environment, make sure you have the necessary VS Code extensions installed.

### **🔹 Installation Steps**  
1. Open **VS Code**  
2. Go to the **Extensions Marketplace** (`Ctrl + Shift + X` on Windows/Linux, `Cmd + Shift + X` on Mac)  
3. Search for and install the following extensions as required:
   - **Python** (by Microsoft)  
   - **Jupyter** (by Microsoft)  
   - **Pylance** (by Microsoft)  
   - **Jupyter Keymap** (by Microsoft)  
   - **Jupyter Notebook Renderers** (by Microsoft)  
   - **Black Formatter** (by Microsoft or Prettier)  
   - **isort** (by Microsoft)  
4. Restart VS Code to ensure all extensions are properly loaded.

---

## **3️⃣ Create and Activate a Virtual Environment**  
1. Open the terminal in VS Code:
    - **MacOS:** **Cmd + Shift + `**
    - **Windows:** **Ctrl + Shift + `**

2. **Create and Activate the Virtual Environment**

    ### **🔹 macOS/Linux**  
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

    ### **🔹 Windows (Command Prompt)**  
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```

    ### **🔹 Windows (PowerShell)**  
    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

**Note:** Ensure your virtual environment is activated before proceeding to the next step.

---

## **4️⃣ Install Dependencies**  
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

---

## **5️⃣ Update VS Code User Preferences (Auto-Format on Save)**  

To ensure **consistent formatting** across your project, you need to update your **User Preferences (`settings.json`)** in VS Code.  

### **🔹 Steps to Update `settings.json`**
1. Open **VS Code**.  
2. Open the **Command Palette** (`Ctrl + Shift + P` on Windows/Linux, `Cmd + Shift + P` on Mac).  
3. Search for **"Preferences: Open Settings (JSON)"** and select it.  
4. Inside the file, find the existing `{}` brackets and **add the following settings inside them**, making sure not to delete any existing settings:
```json
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "python.formatting.provider": "black",
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    }
}
```

---

## **6️⃣ Logging into Customer Seeq Instances Locally**  

Instead of maintaining multiple credential files, this setup allows you to **store all credentials in a single `credentials.json` file** and **seamlessly switch customers** by modifying a single line in `__init__.py`.

Additionally, this method ensures that **local development mirrors production** as closely as possible, making it easier to deploy to customer environments **without code modifications**.

### **🔹 Requirements**
Ensure that the following files exist:  
✅ **`_seeq_login.py`** in the **project root**  
✅ **`__init__.py`** inside each **subproject folder** (e.g., `./customer1/`, `./develop/`)  
✅ **`credentials.json`** in the **project root**, with the following format:

```json
{
    "develop": {
        "server": "https://develop.seeq.dev",
        "access_key": "dev_access_key",
        "password": "dev_password"
    },
    "customer1": {
        "server": "https://customer1.seeq.dev",
        "access_key": "customer1_access_key",
        "password": "customer1_password"
    },
    "customer2": {
        "server": "https://customer2.seeq.dev",
        "access_key": "customer2_access_key",
        "password": "customer2_password"
    }
}
```
### **🔹 Set the Active Customer**
Modify `DEFAULT_CUSTOMER` inside the `__init__.py` file **inside the customer’s folder** (e.g., `./customer1/__init__.py`).  
This ensures each customer has its own authentication settings. 

```python
DEFAULT_CUSTOMER = "customer1"  # Change to "customer2", "develop", etc.
```
**If `DEFAULT_CUSTOMER` is not modified, it will default to `'develop'`.**

---

### **🔹 ⚠️ Do Not Modify `_seeq_login.py`**
`_seeq_login.py` automatically loads credentials based on `DEFAULT_CUSTOMER` within the`__init__.py` file , so you **do not need to modify this file**.

### **🔹 Do Not Upload to Customer Instances**
To prevent accidental uploads, add these files to your `.gitignore`:

```
__init__.py
_seeq_login.py
```

---

## **7️⃣ Using VS Code and Select the Correct Interpreter**  

1. Open **VS Code**.  
2. Open the **Command Palette** (`Ctrl + Shift + P` on Windows/Linux, `Cmd + Shift + P` on Mac).  
3. Type: **Python: Select Interpreter**.  
4. Select the Python interpreter inside your virtual environment:  
   ```
   .venv/bin/python  (Mac/Linux)  
   .venv\Scripts\python.exe  (Windows)  
   ```

When selecting the Python interpreter, **choose the one named `.venv`**.  
If it does not appear in the list, restart VS Code and try again.  

---

## **8️⃣ Running Jupyter in VS Code**  

If you're using **VS Code’s Jupyter extension**, you can open a `.ipynb` file directly within VS Code. However, note that some ipyvuetify components might not render correctly in this environment.

### **Alternative: Launching JupyterLab**  

If you encounter rendering issues with ipyvuetify content or prefer the full browser-based interface, you can launch JupyterLab:

1. Open the terminal in VS Code (**Ctrl/Cmd + Shift + `**).
2. Run the following command:
   ```sh
   jupyter lab
   ```
3. JupyterLab will automatically open in your default web browser. If it doesn’t, you can manually navigate to:
   ```
   localhost:8888/lab
   ```

---

## **9️⃣ Running Voila in JupyterLab to Render an Add-on**

If you are developing an Add-on and want to render the notebook in Add-on Mode, you can install the Jupyter extension `voila-dashboard-jupyterlab-preview`.

### Steps to Install and Use Voila in JupyterLab:

1. Launch JupyterLab by running the following command:
   ```sh
   jupyter lab
   ```

2. Enable the **Extension Manager** within the **Settings** tab.

3. Install the extension `voila-dashboard-jupyterlab-preview`.

4. To render a notebook in Add-on Mode:
   - **Right-click** the desired notebook, select **Open With**, and choose **Voila Preview**.
   - Alternatively, use the **Voila** icon in the Jupyter notebook toolbar to launch the notebook in Add-on Mode.

---

## 🎯 **Troubleshooting**  

### **Issue: Widgets do not render**  
**Fix:** Run:  
```sh
pip install --force-reinstall jupyterlab_widgets widgetsnbextension
```

### **Issue: Jupyter Notebook can't find Python kernel**  
**Fix:** Run:
```sh
python -m ipykernel install --user --name=.venv
```
Then restart VS Code and reselect the Python interpreter.

---

Now, you can **stay within VS Code, leverage GitHub Copilot for assistance, and maintain a single repository of work for all customers**—without needing separate environments or credentials for each one! 🚀
