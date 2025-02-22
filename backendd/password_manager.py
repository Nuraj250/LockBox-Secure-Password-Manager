from backend.db_handler import add_entry, get_entries, delete_entry
from backend.encryption import encrypt_password, decrypt_password

def save_password(website, username, password):
    encrypted_password = encrypt_password(password)
    add_entry(website, username, encrypted_password)

def retrieve_passwords():
    entries = get_entries()
    return [(entry[0], entry[1], entry[2], decrypt_password(entry[3])) for entry in entries]

def remove_password(entry_id):
    delete_entry(entry_id)
