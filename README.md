# 🔒 LockBox Secure Password Manager

LockBox is a **secure and user-friendly password manager** that encrypts stored passwords and provides a **PyQt-based UI** for easy password management.

## 🚀 Features

- ✅ Secure **password storage** with encryption  
- ✅ **User-friendly** PyQt5-based GUI  
- ✅ **Encryption & decryption** using `cryptography`  
- ✅ **SQLite-based local database**  
- ✅ **Password retrieval & management**  
- ✅ **Cross-platform support** (Windows, macOS, Linux)  

---

## 📌 Project Structure

```
lockbox-password-manager/
├── backend/                # Backend logic (encryption, database)
│   ├── db_handler.py       # Database operations (SQLite)
│   ├── encryption.py       # Encryption & decryption logic
│   ├── password_manager.py # Core password management logic
│   ├── settings.py         # Configuration settings
│   ├── __init__.py         # Package initializer
├── frontend/               # GUI components (PyQt-based UI)
│   ├── app.py              # Main application entry point
│   ├── ui_main.py          # GUI layout & interactions
│   ├── assets/             # Icons & resources (if needed)
│   ├── styles/             # UI styles (optional)
│   ├── __init__.py         # Package initializer
├── database/               # Database storage
│   ├── lockbox.db          # SQLite database file
│   ├── migrations/         # Database migration files
│   ├── schema.sql          # Database schema
├── tests/                  # Unit tests
│   ├── test_db.py          # Tests for database operations
│   ├── test_encryption.py  # Tests for encryption module
│   ├── test_ui.py          # Tests for UI interactions
├── docs/                   # Documentation
│   ├── README.md           # Project documentation
│   ├── INSTALL.md          # Installation guide
│   ├── USAGE.md            # Usage instructions
├── requirements.txt        # Dependencies list
├── .gitignore              # Ignore sensitive files
├── LICENSE                 # Open-source license file
├── setup.py                # Setup script for packaging
└── README.md               # Main project README
```

---

## 🔧 Installation Guide

### 📌 Prerequisites
- **Python 3.8+** must be installed.
- Install `pip` if not already available.

### 📌 Steps to Install

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-repo/LockBox-Secure-Password-Manager.git
   cd LockBox-Secure-Password-Manager
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**  
   ```sh
   python frontend/app.py
   ```

---

## 💡 Usage

### 🔑 **Adding a Password**
1. Open the **LockBox** app.
2. Enter the **Website**, **Username**, and **Password**.
3. Click **"Add Password"** to save.

### 🔍 **Viewing Saved Passwords**
- Click **"Refresh List"** to display stored passwords.

### ❌ **Deleting a Password**
- (Feature coming soon in v1.1)

---

## 🔒 Security Measures
- **AES Encryption** via `cryptography` package.
- **Secure SQLite Storage** for passwords.
- **Auto-Encryption** of saved passwords.

---

## 🐜 Contributing

1. **Fork the repository**  
2. **Create a new branch**  
3. **Submit a Pull Request**  

All contributions are welcome! 😊

---

## 💜 License
This project is licensed under the **MIT License**. Feel free to modify and distribute.

---

## 📧 Contact
For questions or suggestions, feel free to **open an issue** or **contact me** via GitHub.

---

🔥 **Developed with ❤️ by Nuraj** 🔥

