from flask import render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from numpy import insert
from werkzeug.security import generate_password_hash
import os

def register_client():
    if request.method == 'POST':
        # img = request.files['image']
        fullname = request.form['fullname']
        email = request.form["email"]
        dni = request.form['dni']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        flag = 0
        img = "img"

        insertUser(fullname, email, hashed_password, dni, flag, img)
        os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')
        return redirect(url_for('login'))
    return render_template('register_page.html')


def insertUser(fullname, email,  password, dni, flag, img):
    mysql = MySQL();
    conn = mysql.connect();
    cursor = conn.cursor();
    sql = "INSERT INTO user (fullname, email, password, dni, flag, img) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(fullname, email, password, dni, flag, img)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Usario registrado")