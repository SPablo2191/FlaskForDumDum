from flask import Flask,request


app = Flask(__name__)

# decorador con su respectiva funcion
@app.route("/")
def index():
    return "holis"

# otra ruta de ejemplo
# decorador con su respectiva funcion
@app.route("/saludar")
def saludar():
    return "saludos"

# una ruta puede recibir parametros
# decorador con su respectiva funcion
@app.route("/params")
def params():
    param = request.args.get('parametro','valor por default')
    # para pasar parametro entonces seria la url?parametro=ElValor a mostrar

    #http://127.0.0.1:8000/params?parametro=pablo --> retornara pablo
    #http://127.0.0.1:8000/params --> retornara valor por defecto 
    return "parametro: {}".format(param)

## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)