def login_userDB(mysql, dni):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = f"SELECT * FROM client WHERE dni = {dni}"
    cursor.execute(sql)
    user = cursor.fetchone()
    return user