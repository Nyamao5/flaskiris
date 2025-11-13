# PythonAnywhere Deployment Guide

## Problem
The error `ModuleNotFoundError: No module named 'numpy._core'` occurs because:
- Your local environment uses **numpy 2.3.4** (which has `numpy._core`)
- PythonAnywhere has an older **numpy 1.x** (which doesn't have `numpy._core`)
- The pickle file created with numpy 2.x is incompatible with numpy 1.x

## Solution: Regenerate Model with Compatible Versions

### Step 1: Install Compatible Versions Locally

```bash
pip install numpy==1.24.3 scikit-learn==1.3.2
```

### Step 2: Regenerate the Model

Run the regeneration script:

```bash
python regenerate_model.py
```

Or run the notebook cell that trains and saves the model.

### Step 3: Deploy to PythonAnywhere

1. **Upload your files** to PythonAnywhere:
   - `app.py`
   - `iris_model.pkl` (the newly generated one!)
   - `requirements.txt`
   - `templates/index.html`

2. **Install dependencies** in PythonAnywhere bash console:
   ```bash
   cd ~/flaskiris
   pip install --user -r requirements.txt
   ```

3. **Configure WSGI file** (`/var/www/tonynyamaootenyo9_pythonanywhere_com_wsgi.py`):
   ```python
   import sys
   
   # Add your project directory to the sys.path
   project_home = '/home/tonynyamaootenyo9/flaskiris'
   if project_home not in sys.path:
       sys.path = [project_home] + sys.path
   
   # Import the Flask app
   from app import app as application
   ```

4. **Reload your web app** in the PythonAnywhere Web tab.

## Updated requirements.txt

The new `requirements.txt` includes only essential packages with compatible versions:

```
Flask==3.1.2
numpy==1.24.3
scikit-learn==1.3.2
joblib==1.3.2
```

## Verification

After deployment, your app should work without errors. The model will correctly predict iris species based on the input features.

## Alternative Solution (If Above Doesn't Work)

If PythonAnywhere has an even older Python version, try these versions:

```
Flask==2.3.0
numpy==1.21.6
scikit-learn==1.0.2
joblib==1.1.0
```

Then regenerate the model again with these versions installed.
