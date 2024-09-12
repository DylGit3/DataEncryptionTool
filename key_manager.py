from cryptography.fernet import Fernet

#generates a key, opens a file in binary format (not string) and creates an object (key_files) to access the key file, writes to the file with the key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

#opens key after reading it in binary format
def load_key() -> bytes:
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

#generate the key one time and then use load_key as needed