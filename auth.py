# auth.py
# Manejo de login y registro

from flask import Blueprint, render_template, request, redirect, session
from models import crear_usuario, obtener_usuario

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = obtener_usuario(username)

        if user and user["password"] == password:

            session["user_id"] = user["id"]

            return redirect("/")

    return render_template("login.html")


@auth.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        crear_usuario(username, password)

        return redirect("/login")

    return render_template("registro.html")


@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")