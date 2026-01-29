from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

import math

app = Flask(__name__)
app.secret_key='Clave secreta'
csrf=CSRFProtect()

@app.route('/')
def index():
    titulo = "IDGS-802-Flask"
    lista = ['juan', 'karina', 'miguel']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''

    mensaje='Bienvenido{}'.format(nom)
    flash(mensaje)

    usuarios_class = forms.UserForm(request.form) 
    
    if request.method == "POST" and usuarios_class.validate(): 
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data


    return render_template("usuarios.html", form=usuarios_class,
                           mat=mat, nom=nom, apa=apa, ama=ama, correo=email)

@app.route('/formularios')
def formularios():
    return render_template("formulario.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "la suma es: {}".format(n1 + n2)

@app.route("/default")
@app.route("/default/<string:param>")
def func2(param="juan"):
    return f"<h1>¡hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </form>
    '''

@app.route("/distancia", methods=["GET","POST"])
def distancia():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    res = 0
    if request.method == "POST":
        x1 = request.form.get("x1")
        x2 = request.form.get("x2")
        y1 = request.form.get("y1")
        y2 = request.form.get("y2")
        res = math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)
    return render_template("distancia.html", res=res)

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    return render_template("alumnos.html")



@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        if n1 and n2:
            res = float(n1) + float(n2)
            
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
            n1 = float(request.form.get("n1"))
            n2 = float(request.form.get("n2"))
            operacion = request.form.get("operacion")
            
            res = 0
            
            if operacion == "suma":
                res = n1 + n2
            elif operacion == "resta":
                res = n1 - n2
            elif operacion == "multi":
                res = n1 * n2
            elif operacion == "div":
                if n2 != 0:
                    res = n1 / n2
                else:
                    return "Error: No se puede dividir entre cero"
            
            return f"El resultado de la {operacion} es: {res}"
            
    return render_template("operasBas.html")

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)