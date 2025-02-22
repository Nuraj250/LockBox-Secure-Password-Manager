import unittest
from backend.encryption import encrypt_password, decrypt_password

class TestEncryption(unittest.TestCase):

    def test_encryption_decryption(self):
        test_password = "MySecurePass123"
        encrypted = encrypt_password(test_password)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(test_password, decrypted)

if __name__ == "__main__":
    unittest.main()
