from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators, BooleanField, RadioField

class UserForm(Form):
    
    matricula=IntegerField('Matricula',[
                validators.DataRequired(message="El campo es requerido"),
                validators.NumberRange(min=0, max=1000,message="Ingrese un valor valido")])
    nombre=StringField("Nombre",[
                validators.DataRequired(message="El campo es requerido"),
                validators.length(min=3, max=10,message="Ingrese nombre valido")])
    apaterno=StringField("Apaterno",[
                validators.DataRequired(message="El campo es requerido")])
    amaterno=StringField("Amaterno",[
                validators.DataRequired(message="El campo es requerido")])
    correo=EmailField('Correo',[
                validators.Email(message="Ingrese un correo Valido")])

class CineForm(Form):
        
        nombre=StringField("Nombre",
            [validators.DataRequired(message="El campo es requerido")])
        compradores=StringField("Compradores",
            [validators.DataRequired("Requiere cantidad de compradores")])
        boletos=StringField("Boletos",
             [validators.DataRequired("Requiere cantidad de boletos")])
        cineco=RadioField("",
            choices=[('si','Sí'),('no','No')],
            validators=[validators.DataRequired("Tienes que seleccionar el cineco")])