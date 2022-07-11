from flask import Flask,request
from flask import render_template

app = Flask(__name__,template_folder="templates")

# decorador con su respectiva funcion
@app.route("/")
def index():
    return render_template("index.html")



## esto se hace por las buenas practicas de python
if __name__ == "__main__":
    app.run(debug=True,port=8000)