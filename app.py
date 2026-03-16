# app.py

from flask import Flask, render_template, request, redirect, session
from models import *

from auth import auth

app = Flask(__name__)

app.secret_key = "clave_super_secreta"

app.register_blueprint(auth)

crear_tablas()


# -------------------
# LANDING
# -------------------

@app.route("/")
def index():

    usuario_logueado = "user_id" in session

    return render_template(
        "index.html",
        usuario_logueado=usuario_logueado
    )


# -------------------
# DASHBOARD
# -------------------

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    animales = obtener_animales(session["user_id"])

    return render_template(
        "dashboard.html",
        animales=animales
    )


# -------------------
# REGISTRAR ANIMAL
# -------------------

@app.route("/registrar_animal",methods=["GET","POST"])
def registrar_animal_view():

    if "user_id" not in session:
        return redirect("/login")

    if request.method=="POST":

        registrar_animal(
            session["user_id"],
            request.form["identificacion"],
            request.form["raza"],
            request.form["fecha_nacimiento"],
            request.form["sexo"]
        )

        return redirect("/dashboard")

    return render_template("registrar_animal.html")


# -------------------
# PERFIL ANIMAL
# -------------------

@app.route("/animal/<id>")
def perfil_animal(id):

    if "user_id" not in session:
        return redirect("/login")

    animal = obtener_animal(id)

    pesos = obtener_pesos(id)

    return render_template(
        "perfil_animal.html",
        animal=animal,
        pesos=pesos
    )


# -------------------
# REGISTRAR PESO
# -------------------

@app.route("/registrar_peso/<id>",methods=["POST"])
def registrar_peso_view(id):

    if "user_id" not in session:
        return redirect("/login")

    peso = request.form["peso"]
    fecha = request.form["fecha"]

    registrar_peso(id,peso,fecha)

    return redirect(f"/animal/{id}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)