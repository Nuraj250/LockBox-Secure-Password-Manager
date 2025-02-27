from backend.db_handler import add_entry, get_entries, delete_entry
from backend.encryption import encrypt_password, decrypt_password

def save_password(website, username, password):
    """
    Step 1: Save a new password
    - Encrypts the given password using Fernet encryption.
    - Stores the encrypted password in the database along with the website and username.
    """
    encrypted_password = encrypt_password(password)  # Encrypt the password
    add_entry(website, username, encrypted_password)  # Save encrypted password in the database

def retrieve_passwords():
    """
    Step 2: Retrieve and decrypt stored passwords
    - Fetches all saved password entries from the database.
    - Decrypts the encrypted password for each entry.
    - Returns a list of tuples containing (ID, Website, Username, Decrypted Password).
    """
    entries = get_entries()  # Fetch all stored entries from the database
    return [(entry[0], entry[1], entry[2], decrypt_password(entry[3])) for entry in entries]  # Decrypt passwords

def remove_password(entry_id):
    """
    Step 3: Remove a stored password entry
    - Takes the entry ID as input.
    - Deletes the corresponding entry from the database.
    """
    delete_entry(entry_id)  # Remove password entry from the database
