# SDD Python Web App 
 
This is a simple Flask web app created using a manual Spec-Driven Development workflow. 
 
## Purpose 
The app displays a static page explaining the benefits of Spec-Driven Development. 
 
## Run locally 
```powershell 
python -m venv .venv 
.\.venv\Scripts\Activate.ps1 
python -m pip install -r requirements.txt 
python app.py 
``` 
 
Open: http://127.0.0.1:5000 
 
## Run tests 
```powershell 
python -m pytest -v 
``` 
 
## SDD artifacts 
See docs/spec-kit/ for constitution, specification, clarifications, plan, tasks, and analyze checklist. 