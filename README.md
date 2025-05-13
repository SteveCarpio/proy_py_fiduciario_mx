# proy_py_fiduciario_mx
Proyecto Python (Flask) para registro de tareas fiduciario

# Compilado:
pyinstaller --onefile --name=app --add-data "templates;templates" --add-data "personas.db;." app.py

pyinstaller --onefile --name=FIDUCIARIO --add-data "templates;templates" --add-data "personas.db;." app.py
