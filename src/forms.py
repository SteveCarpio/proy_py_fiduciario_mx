from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Email

class PersonaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    notas = TextAreaField('Notas')
    fecha_entrada = DateField('Fecha de Entrada', format='%Y-%m-%d', validators=[DataRequired()])
    estado = SelectField('Estado', choices=[
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
        ('reabierto', 'Reabierto')
        ], validators=[DataRequired()])
    enviar = SubmitField('Guardar')
