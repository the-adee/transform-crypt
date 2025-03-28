import os
from cryptography.fernet import Fernet

def generate_and_store_key():
    """Generates a secure random key and stores it in an environment variable."""
    key = Fernet.generate_key().decode()
    os.environ["ENCRYPTION_KEY"] = key  # Store key in environment variable
    return key

def get_secret_key():
    """Retrieves the secret key from the environment variable or generates a new one if missing."""
    return os.getenv("ENCRYPTION_KEY") or generate_and_store_key()
