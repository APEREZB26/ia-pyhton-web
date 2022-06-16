from select import select
from flask import Flask, request
from flask import redirect, url_for, render_template, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug.utils import secure_filename
import os

# Controladores
# from controllers.auth import *
# from controllers.auth.register import register_client

app = Flask(__name__)
app.secret_key = 'elmejorgurpo'  #SECRET KEY

# Conexion a la DB
mysql = MySQL();
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='211926'
app.config['MYSQL_DATABASE_DB']='proyect'
mysql.init_app(app)

@app.route('/')
def index():
    # conn = mysql.connect();
    # cursor = conn.cursor();
    # sql = "SELECT * FROM user WHERE user.id=1"
    # cursor.execute(sql)
    # resultado = cursor.fetchone();
    # conn.close();
    # print("Esots son los usuarios", resultado)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    # return login_user()
    return render_template('login_page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # return register_client()
    if request.method == 'POST':
        # img = request.files['image']
        fullname = request.form['fullname']
        email = request.form["email"]
        dni = request.form['dni']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        flag = 0
        img = "img"

        # DATABASE
        conn = mysql.connect();
        cursor = conn.cursor();
        sql = "INSERT INTO client (fullname, email, password, dni, flag, img) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(fullname, email, hashed_password, dni, flag, img)
        cursor.execute(sql)
        conn.commit()
        conn.close()

        os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')
        return redirect(url_for('login'))
    return render_template('register_page.html')

# @app.route('/client', methods=['GET', 'POST'])
# def client():
#     return render_template('client_page.html')

# @app.route('/admin', methods=['GET'])
# def admin():
#     return render_template('admin_page.html')

# @app.route('/admin/manage/profile', methods=['GET', 'POST'])
# def manageprofileAdmin():
#     try:
#         id = session['id']
#         fullname = session['fullname']
#         return render_template('admin_crud_profile_page.html', id=id, fullname=fullname)
#     except Exception as e:
#         return redirect(url_for('admin'))

@app.route('/admin/manage/listEmpl', methods=['GET', 'POST'])
def listAdmin():
    conn = mysql.connect();
    cursor = conn.cursor();
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    print("Estos son los usuarios",usuarios)
    return render_template('admin_crud_page.html', usuarios=usuarios)

# @app.route('/admin/manage/addEmpl', methods=['POST'])
# def addAdmin():

#     user = Users.query.filter(Users.rol == 1)

#     #Add Admin
#     img = request.files['photo']
#     fullname=request.form["fullname"]
#     email=request.form["email"]
#     dni=request.form["dni"]
#     password=request.form["password"]
#     rol = request.form["rol"]
#     hashed_password = generate_password_hash(password, method='sha256')
#     phone=request.form["phone"]

#     os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')

#     filename = secure_filename(img.filename) #Nombre original del archivo
     
#     upload_path = os.path.join (f'face_recognition_and_liveness/face_recognition/dataset/{dni}', filename) 
#     img.save(upload_path) #Nombre original del archivo  

#     newUser = Users(fullname=fullname, email=email, dni=dni, password=hashed_password, rol=rol,phone=phone)
#     db.session.add(newUser)
#     print(db.session.add(newUser))
#     db.session.commit()

#     return render_template('admin_crud_page.html', id=id, fullname=fullname, users=user)


@app.route('/admin/manage/deleteEmpl/<int:id>')
def deleteAdmin(id):
    conn = mysql.connect();
    cursor = conn.cursor();
    # sql = "DELETE FROM employee WHERE id=%d", (id)
    cursor.execute("DELETE FROM employee WHERE id=%s", (id))
    conn.commit()
    conn.close()
    return render_template('admin_crud_page.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
