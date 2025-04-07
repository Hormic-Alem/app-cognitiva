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
#ejercicio secuencias
@app.route("/ejercicio3", methods=["GET", "POST"])
def ejercicio3():
    if request.method == "POST":
        user_answer = request.form.get("respuesta")
        correcta = int(request.form.get("respuesta_correcta"))

        if user_answer and int(user_answer) == correcta:
            flash("¡Correcto!", "success")
        else:
            flash(f"Incorrecto. La respuesta correcta era: {correcta}", "danger")
        return redirect(url_for("ejercicio3"))

    # Generar secuencia aritmética dinámica
    inicio = random.randint(1, 10)
    paso = random.randint(1, 5)
    longitud = 4

    secuencia = [inicio + i * paso for i in range(longitud)]
    respuesta_correcta = inicio + longitud * paso
    secuencia.append(None)

    return render_template("ejercicio3.html", secuencia=secuencia, respuesta_correcta=respuesta_correcta)


# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
