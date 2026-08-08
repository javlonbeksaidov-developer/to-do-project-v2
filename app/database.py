import sqlite3

FILENAME = "todo.db"


def create():
    with sqlite3.connect(FILENAME) as connection:
        cursor = connection.cursor()
        command = """CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(100), description VARCHAR(255), status BOOLEAN DEFAULT FALSE);"""
        cursor.execute(command)
        connection.commit()


def insert(title, description, status=False):
    with sqlite3.connect(FILENAME) as connection:
        cursor = connection.cursor()
        command = """INSERT INTO todo (title, description, status) VALUES (?, ?, ?);"""
        cursor.execute(command, (title, description, status))
        connection.commit()


def update(id, title, description, status=False):
    with sqlite3.connect(FILENAME) as connection:
        cursor = connection.cursor()
        command = """UPDATE todo SET title=?, description=?, status=? WHERE id=?;"""
        cursor.execute(command, (title, description, status, id))
        connection.commit()


def delete(id):
    with sqlite3.connect(FILENAME) as connection:
        cursor = connection.cursor()
        command = """DELETE FROM todo WHERE id=?;"""
        cursor.execute(command, (id,))
        connection.commit()


def select():
    with sqlite3.connect(FILENAME) as connection:
        cursor = connection.cursor()
        command = """SELECT * FROM todo;"""
        cursor.execute(command)
        return cursor.fetchall()
