from cryptography.fernet import Fernet
from key_manager import load_key

#needs a key to have been generated to work, takes a string message and turns it into an encrypted message using bytes
def encrypt_message(message : str) -> bytes:
    key = load_key()
    f = Fernet(key)
    return f.encrypt(message.encode())

#takes an encrypted bytes message and turns it into a string
def decrypt_message(encrypted_message : bytes) -> str:
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()