from flask import Flask,request


app = Flask(__name__)

# decorador con su respectiva funcion
@app.route("/")
def index():
    return "holis"

# cuando mi ruta recibe parametros sin signo de interrogacion
@app.route("/params/")
@app.route("/params/<name>")
@app.route("/params/<int:name>")
def params(name=''):
    return "hola {}".format(name)

## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)