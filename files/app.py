from flask import Flask,request
from flask import render_template
from forms import CommentForm
app = Flask(__name__,template_folder="templates")

@app.route("/")
def forms():
    comment_form = CommentForm()
    name="pablo"
    return render_template("form.html",name = name, form = comment_form)



# decorador con su respectiva funcion
@app.route("/herencia")
def user():
    name="pablo"
    lista=[1,2,3,4]
    return render_template("indexEstatico.html", name = name,lista = lista)



## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)