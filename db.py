# db.py
import sqlite3

DB_NAME = "texts.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

# Categories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

# Text table with category_id column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
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
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM texts WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def update_text(cursor, conn, text_id, new_content):
    cursor.execute("UPDATE texts SET content = ? WHERE id = ?", (new_content, text_id))
    conn.commit()

# ---------- Categories ----------

def get_all_categories(cursor):
    cursor.execute("SELECT id, name FROM categories ORDER BY name")
    return cursor.fetchall()

def add_category(cursor, conn, name):
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    conn.commit()

def update_text_category(cursor, conn, text_id, category_id):
    cursor.execute("UPDATE texts SET category_id = ? WHERE id = ?", (category_id, text_id))
    conn.commit()
