from flask import request, redirect, url_for
import re

def employee_validation(mysql, fullname, email, dni, password, phone):
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
        return False, " FULLNAME incorrecto"
    else:
        print(regfullname)
        conn = mysql.connect();
        cursor = conn.cursor();
        cursor.execute("SELECT fullname FROM proyect.employee WHERE fullname='{}'".format(fullname))
        fullnameBD = cursor.fetchone()

        if (fullnameBD == None):
            if regemail is None:
                return False, " EMAIL incorrecto"
            else:
                conn = mysql.connect();
                cursor = conn.cursor();
                cursor.execute("SELECT email FROM proyect.employee WHERE email='{}';".format(email))
                emailBD = cursor.fetchone()

                if (emailBD == None):
                    if regdni is None:
                        return False, " DNI incorrecto"
                    else:
                        conn = mysql.connect();
                        cursor = conn.cursor();
                        cursor.execute("SELECT dni FROM proyect.employee WHERE dni={};".format(dni))
                        dniBD = cursor.fetchone()

                        if (dniBD == None):
                            if regphone is None:
                                return False, "PHONE incorrecto"
                            else:
                                conn = mysql.connect();
                                cursor = conn.cursor();
                                cursor.execute("SELECT phone FROM proyect.employee WHERE phone={}".format(phone))
                                phoneBD = cursor.fetchone()
                                if (phoneBD == None):
                                    return True, "Usuario agregado"
                                else:
                                    return False, "PHONE duplicado"
                        else:
                            return False, " DNI duplicado"
                else:
                    return False, " EMAIL duplicado"
        else:
            return False, " FULLNAME duplicado"