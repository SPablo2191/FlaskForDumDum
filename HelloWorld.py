from flask import Flask
#instancia - recibe como parametro __name__
app = Flask(__name__)

# necesitamos un decorador para que me devuelva algo
@app.route('/') #le añado una ruta --> sera la direccion a la cual el usuario pueda acceder en la direccion
def index():
    print(__name__)
    return 'Hola Mundo ANASHE'

## creamos otra ruta
@app.route("/hola")
def hola():
    return "holanda"

## manejo de variables
@app.route("/user/<string:user>")
def user(user):
    return "hola "+user

@app.route("/numero/<int:num>")
def numero(num):
    return "hola: {} ".format(num)

@app.route("/numero/<int:id>/<string:username>")
def login(id,username):
    return "hola: {} ,Id: {} ".format(username,id)

if __name__=="__main__":
    app.run(port=8000, debug=True) # ejecuta el servidor


