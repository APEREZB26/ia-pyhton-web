def register_userDB(mysql, fullname, email, password, dni, flag, urlImage):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO client (fullname, email, password, dni, flag, img) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            fullname, email, password, dni, flag, urlImage
        )
    )
    conn.commit()
    conn.close()

def user_existDB(mysql, email, dni):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM client WHERE dni = {dni} or email = '{email}'")
    user = cursor.fetchone()
    return user

