from email.mime import image
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class ProyectoForm(FlaskForm):
    codigo = StringField('Codigo', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    imagen = StringField('Imagen', validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired()])
    submit = SubmitField('Agregar')