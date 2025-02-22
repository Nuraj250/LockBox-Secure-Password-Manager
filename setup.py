from setuptools import setup, find_packages

setup(
    name="lockbox-secure-password-manager",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        "cryptography",
        "sqlite3"
    ],
    entry_points={
        "console_scripts": [
            "lockbox = frontend.app:main"
        ]
    },
    author="Your Name",
    description="A secure password manager with encryption and a PyQt-based UI",
    license="MIT",
    url="https://github.com/your-repo/LockBox-Secure-Password-Manager"
)
