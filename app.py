from flask import Flask, render_template, redirect, request, jsonify, abort

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/pagina")
def pagina():
    return render_template('pagina.html')    

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

users ={
    1:{"name":"Santiago", "lastname":"Murillo", "email":"santiago.murillo@gmail.com"},
    2:{"name":"Vania", "lastname":"Zurita", "email":"vania.zurita@gmail.com"},
    3:{"name":"Joaquin", "lastname":"Lara", "email":"joaquin.lara@gmail.com"}
}

@app.route("/usuario/<int:user_id>")
def get_user_route(user_id):
    user = users.get(user_id)
    if user is None:
        ##abort(404, description="Usuario no encontrado")
        return jsonify({"error": "Usuario no encontrado"})
    return jsonify(user)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404 - No se encontro el recurso"}), 404
    return "Lo siento no se encontro el recurso"

from flask import session
app.secret_key = "123456"

@app.route("/login", methods=["GET","POST"])
def set_user():
    session["user"] = 'Juan'
    return 'Usuario guardado con exito'
    
@app.route("/usuario_logueado")
def usuario_logueado():
    if "user" in session:
        return f"Usuario logueado: {session['user']}"

@app.route("/portafolio")
def portafolio():
    return render_template('pagina.html')



if __name__ == "__main__":
    app.run(debug=True)