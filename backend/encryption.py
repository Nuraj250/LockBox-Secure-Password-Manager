from cryptography.fernet import Fernet
import os

# Define the key file path
KEY_FILE = "database/key.key"

def generate_key():
    """
    Step 1: Generate a new encryption key
    - Generates a new Fernet encryption key.
    - Saves the key to a file for future use.
    - This key should be securely stored and never shared.
    """
    key = Fernet.generate_key()  # Generate encryption key
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)  # Save the key to a file

def load_key():
    """
    Step 2: Load the encryption key from file
    - Reads the stored encryption key.
    - Returns the key for encrypting and decrypting passwords.
    """
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()  # Read and return the key

def encrypt_password(password):
    """
    Step 3: Encrypt a password
    - Loads the encryption key.
    - Uses Fernet encryption to securely encrypt the password.
    - Returns the encrypted password as a string.
    """
    key = load_key()  # Load the encryption key
    f = Fernet(key)  # Initialize Fernet with the key
    return f.encrypt(password.encode()).decode()  # Encrypt and return as string

def decrypt_password(encrypted_password):
    """
    Step 4: Decrypt a password
    - Loads the encryption key.
    - Uses Fernet decryption to securely decrypt the password.
    - Returns the original plain-text password.
    """
    key = load_key()  # Load the encryption key
    f = Fernet(key)  # Initialize Fernet with the key
    return f.decrypt(encrypted_password.encode()).decode()  # Decrypt and return as string

# Step 5: Ensure the encryption key is generated if it does not exist
if not os.path.exists(KEY_FILE):
    generate_key()
