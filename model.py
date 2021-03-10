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