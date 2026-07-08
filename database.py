import sqlite3

DATABASE = "chat.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_message(role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(role,content) VALUES(?,?)",
        (role, content)
    )

    conn.commit()
    conn.close()


def get_messages():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,content
        FROM messages
        ORDER BY id
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "role": row["role"],
            "content": row["content"]
        }
        for row in rows
    ]


def clear_messages():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages")

    conn.commit()

    conn.close()