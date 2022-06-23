from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from services.auth.registerUser import register_userDB, user_existDB
from utils.uploadCloudinary import upload_image
import requests
import os

from utils.validationRegister import validRegister


def user_register(mysql):
    fullname = request.form["fullname"]
    email = request.form["email"]
    dni = request.form["dni"]
    password = generate_password_hash(request.form["password"], method="sha256")
    flag = 0
    image = request.files["photo"]

    # Validar
    isValid = validRegister(fullname, email, password, dni, image)
    if not (isValid):
        return render_template(
            "register_page.html",
            message="Error en los campos ingresados",
        )

    user = user_existDB(mysql, email, dni)

    if user:
        return render_template("register_page.html", message="El usuario ya existe")

    # Guardar en Cloudinary
    upload_result = upload_image(image, dni)
    urlImage = str(upload_result["secure_url"])

    # Guarda en la BD
    register_userDB(mysql, fullname, email, password, dni, flag, urlImage)

    # Guardar en local
    os.mkdir(f"face_recognition_and_liveness/face_recognition/dataset/{dni}")
    f = open(
        f"face_recognition_and_liveness/face_recognition/dataset/{dni}/{secure_filename(image.filename)}",
        "wb",
    )
    response = requests.get(urlImage)
    f.write(response.content)
    os.system("Codificador.bat")
    f.close()

    return redirect(url_for("login"))
