import random
from flask import Flask, render_template, request, redirect, url_for, flash

# Crear la instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Clave secreta para las sesiones

# Ruta para la página principal (index)
@app.route("/")
def index():
    return render_template("index.html", title="Página principal")

# Ruta para el ejercicio 1
@app.route("/ejercicio1")
def ejercicio1():
    return render_template("ejercicio1.html")

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
