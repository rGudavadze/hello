import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """
        INSERT INTO users(
            username,
            password,
            fav_color
        )VALUES(
            "jaytatum",
            "boston",
            "green"
        );
    """
)

cursor.execute(
    """
        INSERT INTO users(
            username,
            password,
            fav_color
        )VALUES(
            "jaybrown",
            "boston",
            "brown"
        );
    """
)

connection.commit()
cursor.close()
connection.close()