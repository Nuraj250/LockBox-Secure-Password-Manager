import sqlite3

DB_FILE = "database/lockbox.db"

def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        website TEXT,
                        username TEXT,
                        password TEXT
                    )''')
    conn.commit()
    conn.close()

def add_entry(website, username, password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, password))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    entries = cursor.fetchall()
    conn.close()
    return entries

def delete_entry(entry_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE id=?", (entry_id,))
    conn.commit()
    conn.close()

# Ensure the database table is created when the module is imported
create_table()
