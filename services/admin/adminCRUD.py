def list_employeeDB(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    return usuarios


def add_employeeDB(mysql, fullname, email, dni, password, phone, flag, urlImage):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employee (fullname, email, password, dni, phone, flag, img) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (fullname, email, password, dni, phone, flag, urlImage),
    )
    conn.commit()
    conn.close()


def get_employeeDB(mysql, id):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE id = {}".format(id)
    cursor.execute(sql)
    user = cursor.fetchone()
    conn.close()
    return user


def update_employeeDB(mysql, id, phone):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE employee SET phone='{}' WHERE id='{}'".format(phone, id))
    conn.commit()
    conn.close()


def delete_employeeDB(mysql, id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE id=%s", (id))
    conn.commit()
    conn.close()
