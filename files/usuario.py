from flask import Flask,request
from flask import render_template

app = Flask(__name__,template_folder="templates")

# decorador con su respectiva funcion
@app.route("/user/<name>")
def user(name='pablo'):
    lista=[1,2,3,4]
    return render_template("user.html", name = name,lista = lista)



## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)