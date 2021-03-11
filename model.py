import sqlite3

def show_color(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT fav_color FROM users WHERE username='{username}' ORDER BY pk DESC;""")
    color = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = f"{username}'s favourite color is {color}"
    return message

def check_pw(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""")
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password


def signup(username, password, fav_color):
    connection = sqlite3.connect("flask_tut.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT password FROM users WHERE username='{username}';""")
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(f"""INSERT INTO users (username, password, fav_color)
        VALUES('{username}', '{password}', '{fav_color}');""")

        connection.commit()
        cursor.close()
        connection.close()
    else:
        return "User already exist!!!"
    
    return "You've succesfully signed up"

    connection.commit()
    cursor.close()
    connection.close()


def check_users():
    connection = sqlite3.connect("flask_tut.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users
