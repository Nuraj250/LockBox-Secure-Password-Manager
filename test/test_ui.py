import unittest
from PyQt5.QtWidgets import QApplication
from frontend.ui_main import PasswordManagerApp

app = QApplication([])  # Initialize the app

class TestUI(unittest.TestCase):

    def test_ui_initialization(self):
        window = PasswordManagerApp()
        self.assertIsNotNone(window)

if __name__ == "__main__":
    unittest.main()
