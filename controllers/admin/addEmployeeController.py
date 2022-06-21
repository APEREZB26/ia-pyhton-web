from flask import request, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from utils.uploadCloudinary import upload_image
from services.admin.adminCRUD import add_employeeDB
import requests
import os

def add_employee(mysql):
    fullname = request.form["fullname"]
    email= request.form["email"]
    dni= request.form["dni"]
    password= generate_password_hash(request.form["password"], method='sha256')
    phone= request.form["phone"]
    img = request.files['photo']

    # Guardar en Cloudinary
    upload_result = upload_image(img, dni)
    urlImage = str(upload_result['secure_url'])

     # Guarda en la BD
    add_employeeDB(mysql, fullname, email, dni, password, phone, 1, urlImage)

    # Guardar en local
    os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')
    f = open(f'face_recognition_and_liveness/face_recognition/dataset/{dni}/{secure_filename(img.filename)}','wb')
    response = requests.get(urlImage)
    f.write(response.content)
    os.system("Codificador.bat")
    f.close()