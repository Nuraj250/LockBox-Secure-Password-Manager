import sys
from PyQt5.QtWidgets import QApplication
from frontend.ui_main import PasswordManagerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())
