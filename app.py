from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/bienvenida")
def bienvenida():
    return render_template('bienvenida.html')

if __name__ == "__main__":
    app.run(debug=True)