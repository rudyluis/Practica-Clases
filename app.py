from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/bienvenida")
def bienvenida():
    return render_template('bienvenida.html')

@app.route("/usuario/<name>")
def user(name):
    return f"<h1>hola {name}</h1>"

@app.route("/direccion")
def redireccionar():
    return redirect("http://www.univalle.edu")

@app.route('/buscar')
def buscar():
    query = request.args.get('q', 'Nada encontrado')
    return f"Buscar: {query}"


if __name__ == "__main__":
    app.run(debug=True)