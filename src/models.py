from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    notas = db.Column(db.Text)
    fecha_entrada = db.Column(db.Date)
    estado = db.Column(db.String(20))
