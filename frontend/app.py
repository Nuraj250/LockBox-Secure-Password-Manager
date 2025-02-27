import sys
from PyQt5.QtWidgets import QApplication
from frontend.ui_main import PasswordManagerApp  # Import the main UI class

# Step 1: Entry point of the application
if __name__ == "__main__":
    # Step 2: Create a PyQt5 application instance
    app = QApplication(sys.argv)

    # Step 3: Initialize the main window (Password Manager UI)
    window = PasswordManagerApp()
    
    # Step 4: Display the main window
    window.show()

    # Step 5: Execute the application event loop
    sys.exit(app.exec_())  # Ensures proper application termination
