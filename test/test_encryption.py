import unittest
from backend.encryption import encrypt_password, decrypt_password

class TestEncryption(unittest.TestCase):
    """
    Unit tests for the encryption and decryption functions in encryption.py
    """

    def test_encryption_decryption(self):
        """
        Step 1: Test password encryption and decryption
        - Encrypts a sample password ("MySecurePass123").
        - Decrypts the encrypted password.
        - Asserts that the decrypted password matches the original input.
        """
        test_password = "MySecurePass123"  # Sample password
        encrypted = encrypt_password(test_password)  # Encrypt the password
        decrypted = decrypt_password(encrypted)  # Decrypt the password

        # Ensure decrypted password matches the original
        self.assertEqual(test_password, decrypted)

if __name__ == "__main__":
    unittest.main()
