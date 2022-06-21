from flask import Flask, request, redirect, url_for, render_template, session
from flask_cors import CORS
from flaskext.mysql import MySQL

# Controllers and services
from controllers.auth.loginController import user_login
from controllers.auth.registerController import user_register
from controllers.admin.addEmployeeController import add_employee
from services.admin.adminCRUD import *

import cloudinary
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)
app.secret_key = 'elmejorgurpo'  #SECRET KEY
CORS(app)

# Conexion a la DB
mysql = MySQL();
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='sebas2001'
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
    if request.method == 'POST':
        return user_login(mysql)

    return render_template('login_page.html')


# Register Client
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return user_register(mysql)

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
    if request.method == 'GET':
        usuarios = list_employeeDB(mysql)

    return render_template('admin_crud_page.html', usuarios=usuarios)

# Employee create
@app.route('/admin/manage/addEmpl', methods=['POST'])
def addAdmin():
    if request.method == 'POST':
        add_employee(mysql)

    return redirect(url_for('listAdmin'))


# Employee get for id
@app.route('/admin/manage/getEmpl/<int:id>')
def getAdmin(id):
    user = get_employeeDB(mysql, id)

    return render_template('admin_edit_user.html', user=user)


# Employee update
@app.route('/admin/manage/updateEmpl/<int:id>', methods=['POST'])
def updateAdmin(id):
    phone = request.form["phone"]
    update_employeeDB(mysql, id, phone)

    return redirect(url_for('listAdmin'))


# Employee delete
@app.route('/admin/manage/deleteEmpl/<int:id>')
def deleteAdmin(id):
    delete_employeeDB(mysql, id)

    return redirect(url_for('listAdmin'))


# === LOGOUT ===
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
