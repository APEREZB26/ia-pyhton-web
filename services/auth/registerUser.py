


def register_userDB(mysql, fullname, email, password, dni, flag, urlImage):
    conn = mysql.connect();
    cursor = conn.cursor();
    cursor.execute("INSERT INTO client (fullname, email, password, dni, flag, img) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(fullname, email, password, dni, flag, urlImage))
    conn.commit()
    conn.close()