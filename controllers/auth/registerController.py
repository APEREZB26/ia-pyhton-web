from flask import request, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from services.auth.registerUser import register_userDB
from utils.uploadCloudinary import upload_image
import requests
import os

def user_register(mysql):
    fullname = request.form['fullname']
    email = request.form["email"]
    dni = request.form['dni']
    password = generate_password_hash(request.form['password'], method='sha256')
    flag = 0
    img = request.files['photo']
    f = open("dni.txt", "w")
    f.write(dni) 
    f.close()

    # Guardar en Cloudinary
    upload_result = upload_image(img, dni)
    urlImage = str(upload_result['secure_url'])

    # Guarda en la BD
    register_userDB(mysql, fullname, email, password, dni, flag ,urlImage)

    # Guardar en local
    os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')
    f = open(f'face_recognition_and_liveness/face_recognition/dataset/{dni}/{secure_filename(img.filename)}','wb')
    response = requests.get(urlImage)
    f.write(response.content)
    os.system("Codificador.bat")
    f.close()

    return redirect(url_for('login'))