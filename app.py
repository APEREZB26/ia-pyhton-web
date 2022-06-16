from flask import Flask, request, redirect, url_for, render_template, session
from flask_cors import CORS
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness
import requests

import cloudinary
import cloudinary.uploader
import cloudinary.api

import os



app = Flask(__name__)
app.secret_key = 'elmejorgurpo'  #SECRET KEY
CORS(app)

# Conexion a la DB
mysql = MySQL();
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='211926'
app.config['MYSQL_DATABASE_DB']='proyect'
mysql.init_app(app)

cloudinary.config( 
  cloud_name = "awdw", 
  api_key = "249828171516131", 
  api_secret = "hqKtXEr0J1nu4G2bbaF3rJNE8yY",
  secure = True
)

@app.route('/')
def index():
    return redirect(url_for('login'))

# === AUTH ===
# Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    if request.method == 'POST':
        dni = request.form['dni']
        password = request.form['password']

        conn = mysql.connect();
        cursor = conn.cursor();
        sql = f'SELECT * FROM client WHERE dni = {dni}'
        cursor.execute(sql)
        user = cursor.fetchone()
        print("user_dni: ", user[4])
        
        if user and check_password_hash(user[3], password):
            detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                             'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                             'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                             'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                             confidence=0.5)
            print("detected_name: ",detected_name)
            print("label_name: ",label_name)
            print("user_dni: ", user[4])
            if user[4] == detected_name and label_name == 'real' and user[5] == 1:
                session['id'] = user[0]
                session['fullname'] = user[1]
                return redirect(url_for('admin'))
            elif user[4] == detected_name and label_name == 'real' and user[5]== 0:
                session['id'] = user[0]
                session['fullname'] = user[1]
                print("session: ", session['id'])
                return redirect(url_for('client'))
            else:
                return render_template('login_page.html', invalid_user=True, username=user[1])
        else:
            return render_template('login_page.html', incorrect=True)
    return render_template('login_page.html')


# Register Client
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form["email"]
        dni = request.form['dni']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        flag = 0
        img = request.files['photo']

        # Guardar en Cloudinary
        upload_result = cloudinary.uploader.upload(img, public_id = dni)
        urlImage = str(upload_result['secure_url'])
        conn = mysql.connect();
        cursor = conn.cursor();
        cursor.execute("INSERT INTO client (fullname, email, password, dni, flag, img) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(fullname, email, hashed_password, dni, flag, urlImage))
        conn.commit()
        conn.close()

        # Guardar en local
        os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')
        f = open(f'face_recognition_and_liveness/face_recognition/dataset/{dni}/{secure_filename(img.filename)}','wb')
        response = requests.get(urlImage)
        f.write(response.content)
        f.close()

        return redirect(url_for('login'))
    return render_template('register_page.html')

@app.route('/client', methods=['GET', 'POST'])
def client():
    return render_template('client_page.html')

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin_page.html')


# === CRUD EMPLOYEE ===
# Employee list
@app.route('/admin/manage/listEmpl', methods=['GET', 'POST'])
def listAdmin():
    conn = mysql.connect();
    cursor = conn.cursor();
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    usuarios = cursor.fetchall()

    return render_template('admin_crud_page.html', usuarios=usuarios)

# Employee create
@app.route('/admin/manage/addEmpl', methods=['POST'])
def addAdmin():
    fullname = request.form["fullname"]
    flag = 1
    email=request.form["email"]
    dni=request.form["dni"]
    password=request.form["password"]
    hashed_password = generate_password_hash(password, method='sha256')
    phone=request.form["phone"]
    img = request.files['photo']

    # Guardar en Cloudinary
    upload_result = cloudinary.uploader.upload(img, public_id = dni)
    urlImage = str(upload_result['secure_url'])
    conn = mysql.connect();
    cursor = conn.cursor();
    cursor.execute('INSERT INTO employee (fullname, email, password, dni, phone, flag, img) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    (fullname, email, hashed_password, dni, phone, flag, urlImage))
    conn.commit()
    conn.close()

    # Guardar en local
    os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/admin/{dni}')
    f = open(f'face_recognition_and_liveness/face_recognition/dataset/admin/{dni}/{secure_filename(img.filename)}','wb')
    response = requests.get(urlImage)
    f.write(response.content)
    f.close()

    return redirect(url_for('listAdmin'))



# Employee get for id
@app.route('/admin/manage/getEmpl/<int:id>')
def getAdmin(id):
    conn = mysql.connect();
    cursor = conn.cursor();
    sql = "SELECT * FROM employee WHERE id = {}".format(id)
    cursor.execute(sql)
    user = cursor.fetchone()
    conn.close()
    print("Estos son los users",user)

    return render_template('admin_edit_user.html', user=user)


# Employee update
@app.route('/admin/manage/updateEmpl/<int:id>', methods=['POST'])
def updateAdmin(id):
    phone = request.form["phone"]
    conn = mysql.connect();
    cursor = conn.cursor();
    cursor.execute("UPDATE employee SET phone='{}' WHERE id='{}'".format(phone, id))
    conn.commit()
    conn.close()

    return redirect(url_for('listAdmin'))


# Employee delete
@app.route('/admin/manage/deleteEmpl/<int:id>')
def deleteAdmin(id):
    conn = mysql.connect();
    cursor = conn.cursor();
    # sql = "DELETE FROM employee WHERE id=%d", (id)
    cursor.execute("DELETE FROM employee WHERE id=%s", (id))
    conn.commit()
    conn.close()

    return redirect(url_for('listAdmin'))


# === LOGOUT ===
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
