import sys
import os

def resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, adaptada para PyInstaller."""
    try:
        base_path = sys._MEIPASS  # Carpeta temporal de PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Entorno normal (dev)

    return os.path.join(base_path, relative_path)

# --------------------------------------

from flask import Flask, render_template, redirect, url_for
from models import db, Persona
from forms import PersonaForm

# Creamos la instancia principal de la aplicación Flask
#app = Flask(__name__)
app = Flask(__name__, template_folder=resource_path('templates'))

app.config['SECRET_KEY'] = '123456'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personas.db'
db_path = os.path.join(os.path.dirname(__file__), 'personas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivamos el rastreo de modificaciones del objeto (mejora rendimiento)

# Asociamos la app Flask con SQLAlchemy
db.init_app(app)

# Este bloque asegura que se cree la base de datos y las tablas si no existen
with app.app_context():
    db.create_all()

# Definimos la ruta principal ("/") que acepta GET y POST
@app.route('/', methods=['GET', 'POST'])
def index():
    # Creamos una instancia del formulario
    form = PersonaForm()

    # Si el formulario fue enviado y es válido...
    if form.validate_on_submit():
        # Creamos una nueva Persona con los datos ingresados
        persona = Persona(
            nombre=form.nombre.data, 
            correo=form.correo.data,
            notas=form.notas.data,
            fecha_entrada=form.fecha_entrada.data,
            estado=form.estado.data
        )

        # Agregamos la nueva persona a la base de datos
        db.session.add(persona)
        db.session.commit()

        # Redirigimos al usuario a la página de registros
        return redirect(url_for('registros'))

    # Si es una solicitud GET o el formulario es inválido, mostramos el formulario
    return render_template('index.html', form=form)

# Definimos la ruta para ver los registros guardados
@app.route('/registros')
def registros():
    # Consultamos todas las personas en la base de datos
    personas = Persona.query.all()

    # Renderizamos la plantilla con los datos
    return render_template('records.html', personas=personas)

# Ejecutamos la aplicación si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
