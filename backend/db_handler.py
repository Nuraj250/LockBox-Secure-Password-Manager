import sqlite3

# Define the database file path
DB_FILE = "database/lockbox.db"

def create_table():
    """
    Step 1: Create a table if it doesn't exist
    - Connects to the SQLite database.
    - Creates a 'passwords' table with columns: id (primary key), website, username, and password.
    - Ensures the table is available before performing operations.
    """
    conn = sqlite3.connect(DB_FILE)  # Connect to database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        website TEXT,
                        username TEXT,
                        password TEXT
                    )''')  # Execute SQL command to create table
    conn.commit()  # Save changes
    conn.close()  # Close connection

def add_entry(website, username, password):
    """
    Step 2: Add a new password entry
    - Takes website, username, and password as input parameters.
    - Inserts the data into the 'passwords' table.
    - Commits the transaction to save changes.
    """
    conn = sqlite3.connect(DB_FILE)  # Connect to database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, password))  # Insert data
    conn.commit()  # Save changes
    conn.close()  # Close connection

def get_entries():
    """
    Step 3: Retrieve all stored password entries
    - Connects to the database.
    - Fetches all records from the 'passwords' table.
    - Returns a list of tuples containing stored passwords.
    """
    conn = sqlite3.connect(DB_FILE)  # Connect to database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute("SELECT * FROM passwords")  # Select all records
    entries = cursor.fetchall()  # Fetch all records
    conn.close()  # Close connection
    return entries  # Return list of stored entries

def delete_entry(entry_id):
    """
    Step 4: Delete a specific password entry
    - Takes an entry ID as an input parameter.
    - Deletes the corresponding row from the 'passwords' table.
    - Commits the transaction to save changes.
    """
    conn = sqlite3.connect(DB_FILE)  # Connect to database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute("DELETE FROM passwords WHERE id=?", (entry_id,))  # Delete specific entry by ID
    conn.commit()  # Save changes
    conn.close()  # Close connection

# Step 5: Ensure the database table is created when the module is imported
create_table()
