from cryptography.fernet import Fernet
from key_manager import load_key

#needs a key to have been generated to work
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    

