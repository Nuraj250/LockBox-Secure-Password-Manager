import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from backend.password_manager import save_password, retrieve_passwords, remove_password

class PasswordManagerApp(QWidget):
    def __init__(self):
        """
        Step 1: Initialize the Password Manager Application
        - Sets the window title, size, and layout.
        - Calls `init_ui()` to build the user interface.
        """
        super().__init__()
        self.setWindowTitle("LockBox Password Manager")  # Set window title
        self.setGeometry(300, 200, 500, 400)  # Set window position and size
        self.init_ui()  # Initialize UI components

    def init_ui(self):
        """
        Step 2: Build the User Interface
        - Creates input fields for website, username, and password.
        - Adds buttons to save passwords and refresh the list.
        - Displays stored passwords in a table.
        """
        layout = QVBoxLayout()  # Create a vertical layout

        # Step 2.1: Input fields for entering password details
        self.website_input = QLineEdit(self)
        self.website_input.setPlaceholderText("Website")
        layout.addWidget(self.website_input)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        layout.addWidget(self.password_input)

        # Step 2.2: Buttons for adding and refreshing password entries
        self.add_button = QPushButton("Add Password", self)
        self.add_button.clicked.connect(self.add_password)  # Connect button to function
        layout.addWidget(self.add_button)

        self.refresh_button = QPushButton("Refresh List", self)
        self.refresh_button.clicked.connect(self.load_passwords)  # Connect button to function
        layout.addWidget(self.refresh_button)

        # Step 2.3: Table to display stored passwords
        self.password_table = QTableWidget()
        self.password_table.setColumnCount(4)  # Define 4 columns
        self.password_table.setHorizontalHeaderLabels(["ID", "Website", "Username", "Password"])
        layout.addWidget(self.password_table)

        # Step 2.4: Set the layout and load existing passwords
        self.setLayout(layout)
        self.load_passwords()  # Load stored passwords on startup

    def add_password(self):
        """
        Step 3: Save a new password entry
        - Retrieves user input for website, username, and password.
        - Calls `save_password()` to store the data.
        - Clears input fields after saving.
        - Refreshes the table to show the new entry.
        """
        website = self.website_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if website and username and password:
            save_password(website, username, password)  # Encrypt and store password
            self.website_input.clear()
            self.username_input.clear()
            self.password_input.clear()
            self.load_passwords()  # Refresh table to show new data

    def load_passwords(self):
        """
        Step 4: Load and display stored passwords
        - Fetches all password entries from the database.
        - Populates the table with decrypted passwords.
        """
        self.password_table.setRowCount(0)  # Clear the table before reloading
        passwords = retrieve_passwords()  # Retrieve saved passwords

        for row_num, (id, website, username, password) in enumerate(passwords):
            self.password_table.insertRow(row_num)  # Insert a new row
            self.password_table.setItem(row_num, 0, QTableWidgetItem(str(id)))  # ID column
            self.password_table.setItem(row_num, 1, QTableWidgetItem(website))  # Website column
            self.password_table.setItem(row_num, 2, QTableWidgetItem(username))  # Username column
            self.password_table.setItem(row_num, 3, QTableWidgetItem(password))  # Password column (decrypted)

# Step 5: Run the PyQt5 Application
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    window = PasswordManagerApp()  # Initialize the main window
    window.show()  # Show the UI
    sys.exit(app.exec_())  # Start the event loop
