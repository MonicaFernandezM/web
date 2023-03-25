from flask import Flask

app = Flask(__name__)

@app.route("/") #punto de salida lo que hay dentro del parentesis 
def la_funcion():
    return "Hola, mundo!"


@app.route("/bye/<nombre>")
def otra_funcion(nombre):
    return f"hasta luego {nombre}"