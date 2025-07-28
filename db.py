# db.py
import sqlite3

DB_NAME = "texts.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn, cursor

def add_text(cursor, conn, content):
    cursor.execute("INSERT INTO texts (content) VALUES (?)", (content,))
    conn.commit()

def get_all_texts(cursor):
    cursor.execute("SELECT id, content FROM texts")
    return cursor.fetchall()

def delete_text(cursor, conn, text_id):
    cursor.execute("DELETE FROM texts WHERE id=?", (text_id,))
    conn.commit()

def search_texts(query):
    conn = sqlite3.connect("texts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM texts WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    return results
