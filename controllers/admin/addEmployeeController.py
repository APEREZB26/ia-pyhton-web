from flask import request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from utils.uploadCloudinary import upload_image
from services.admin.adminCRUD import add_employeeDB
from utils.validationCrud import employee_validation_add, employee_validation_edit
from services.admin.adminCRUD import *
import requests
import os


def edit_employee(mysql, id):
    phone = request.form["phone"]

    # Validación
    isValid, message = employee_validation_edit(mysql, phone)

    if isValid == True:
        update_employeeDB(mysql, id, phone)
        return message
    else:
        return message
    _


def add_employee(mysql):
    fullname = request.form["fullname"]
    email = request.form["email"]
    dni = request.form["dni"]
    password = generate_password_hash(request.form["password"], method="sha256")
    phone = request.form["phone"]
    img = request.files["photo"]

    # Validación
    isValid, message = employee_validation_add(
        mysql, fullname, email, dni, password, phone
    )

    if isValid == True:
        # Guardar en Cloudinary
        upload_result = upload_image(img, dni)
        urlImage = str(upload_result["secure_url"])

        # Guarda en la BD
        add_employeeDB(mysql, fullname, email, dni, password, phone, 1, urlImage)

        # Guardar en local
        os.mkdir(f"face_recognition_and_liveness/face_recognition/dataset/{dni}")
        f = open(
            f"face_recognition_and_liveness/face_recognition/dataset/{dni}/{secure_filename(img.filename)}",
            "wb",
        )
        response = requests.get(urlImage)
        f.write(response.content)
        os.system("Codificador.bat")
        f.close()
        return message
    else:
        return message
