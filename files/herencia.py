from unicodedata import name
from flask import Flask,request
from flask import render_template

app = Flask(__name__,template_folder="templates")

# decorador con su respectiva funcion
@app.route("/")
def user():
    name="pablo"
    return render_template("indexHerencia.html", name = name)

@app.route("/client")
def client():
    lista=["t1","t2","t3","t4"]
    return render_template("client.html", lista = lista)



## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)