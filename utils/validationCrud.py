from flask import request, redirect, url_for
import re

def employee_validation_edit(mysql, phone):
    phone=request.form["phone"]
    exphone = re.compile("^[0-9]{9,9}")
    regphone = exphone.search(phone)

    if regphone is None:
        return False, "Error : El teléfono es incorrecto"
    else:
        conn = mysql.connect();
        cursor = conn.cursor();
        cursor.execute("SELECT phone FROM proyect.employee WHERE phone={}".format(phone))
        phoneBD = cursor.fetchone()
        if (phoneBD == None):
            return True, "Telefono actualizado exitosamente"
        else:
            return False, "Error : El telefono ya existe"
    
def employee_validation_add(mysql, fullname, email, dni, password, phone):
    fullname = request.form["fullname"]
    exfullname = re.compile("^[a-zA-ZÀ-ÿ\s]{1,40}$")
    regfullname = exfullname.search(fullname)

    email=request.form["email"]
    exemail = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    regemail = exemail.search(email)

    dni=request.form["dni"]
    exdni = re.compile("^[0-9]{8,8}")
    regdni = exdni.search(dni)

    password=request.form["password"]

    phone=request.form["phone"]
    exphone = re.compile("^[0-9]{9,9}")
    regphone = exphone.search(phone)

    # Validaciones con regex
    if regfullname is None:
        return False, "Error : El nombre es incorrecto"
    else:
        print(regfullname)
        conn = mysql.connect();
        cursor = conn.cursor();
        cursor.execute("SELECT fullname FROM proyect.employee WHERE fullname='{}'".format(fullname))
        fullnameBD = cursor.fetchone()

        if (fullnameBD == None):
            if regemail is None:
                return False, "Error : El email es incorrecto"
            else:
                conn = mysql.connect();
                cursor = conn.cursor();
                cursor.execute("SELECT email FROM proyect.employee WHERE email='{}';".format(email))
                emailBD = cursor.fetchone()

                if (emailBD == None):
                    if regdni is None:
                        return False, "Error : El DNI es incorrecto"
                    else:
                        conn = mysql.connect();
                        cursor = conn.cursor();
                        cursor.execute("SELECT dni FROM proyect.employee WHERE dni={};".format(dni))
                        dniBD = cursor.fetchone()

                        if (dniBD == None):
                            if regphone is None:
                                return False, "Error : El teléfono es incorrecto"
                            else:
                                conn = mysql.connect();
                                cursor = conn.cursor();
                                cursor.execute("SELECT phone FROM proyect.employee WHERE phone={}".format(phone))
                                phoneBD = cursor.fetchone()
                                if (phoneBD == None):
                                    return True, "Empleado creado exitosamente"
                                else:
                                    return False, "Error : El telefono ya existe"
                        else:
                            return False, "Error : El DNI ya existe"
                else:
                    return False, "Error : El email ya existe"
        else:
            return False, "Error : El nombre ya existe"