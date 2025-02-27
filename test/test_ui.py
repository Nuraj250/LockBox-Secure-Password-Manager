import unittest
from PyQt5.QtWidgets import QApplication
from frontend.ui_main import PasswordManagerApp

# Step 1: Initialize the QApplication instance (needed for PyQt5 UI testing)
app = QApplication([])  

class TestUI(unittest.TestCase):
    """
    Unit tests for the Password Manager UI (PyQt5)
    """

    def test_ui_initialization(self):
        """
        Step 2: Test UI Initialization
        - Creates an instance of `PasswordManagerApp`.
        - Asserts that the window instance is successfully created.
        """
        window = PasswordManagerApp()  # Initialize the main UI window
        self.assertIsNotNone(window)  # Ensure that the window is not None

if __name__ == "__main__":
    unittest.main()
