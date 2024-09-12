from encryption import encrypt_message, decrypt_message
from key_manager import load_key, generate_key

def main():
    # Prompt the user to either generate a new key or load an existing one
    choice = input("Do you want to generate a new encryption key? (yes/no): ").lower()
    
    if choice == "yes":
        generate_key()  # Generate and save a new key
        print("New encryption key generated and saved.")
    else:
        print("Using existing encryption key.")
    
    # Load the saved encryption key
    key = load_key()
    print(f"Encryption key loaded: {key}")
    
    # Prompt user for a message to encrypt
    message = input("Enter the message you want to encrypt: ")
    
    # Encrypt the message
    encrypted_message = encrypt_message(message)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()