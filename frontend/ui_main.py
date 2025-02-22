import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from backend.password_manager import save_password, retrieve_passwords, remove_password

class PasswordManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LockBox Password Manager")
        self.setGeometry(300, 200, 500, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input fields
        self.website_input = QLineEdit(self)
        self.website_input.setPlaceholderText("Website")
        layout.addWidget(self.website_input)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        layout.addWidget(self.password_input)

        # Buttons
        self.add_button = QPushButton("Add Password", self)
        self.add_button.clicked.connect(self.add_password)
        layout.addWidget(self.add_button)

        self.refresh_button = QPushButton("Refresh List", self)
        self.refresh_button.clicked.connect(self.load_passwords)
        layout.addWidget(self.refresh_button)

        # Table
        self.password_table = QTableWidget()
        self.password_table.setColumnCount(4)
        self.password_table.setHorizontalHeaderLabels(["ID", "Website", "Username", "Password"])
        layout.addWidget(self.password_table)

        self.setLayout(layout)
        self.load_passwords()

    def add_password(self):
        website = self.website_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        if website and username and password:
            save_password(website, username, password)
            self.website_input.clear()
            self.username_input.clear()
            self.password_input.clear()
            self.load_passwords()

    def load_passwords(self):
        self.password_table.setRowCount(0)
        passwords = retrieve_passwords()
        for row_num, (id, website, username, password) in enumerate(passwords):
            self.password_table.insertRow(row_num)
            self.password_table.setItem(row_num, 0, QTableWidgetItem(str(id)))
            self.password_table.setItem(row_num, 1, QTableWidgetItem(website))
            self.password_table.setItem(row_num, 2, QTableWidgetItem(username))
            self.password_table.setItem(row_num, 3, QTableWidgetItem(password))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())
