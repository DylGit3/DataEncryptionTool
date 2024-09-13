from encryption import encrypt_message, decrypt_message
from key_manager import load_key, generate_key

def main():
    #prompt the user to either generate a new key or load an existing one
    while True:
        choice = input("Do you want to generate a new encryption key? (yes/no): ").lower()
    
        if choice == "yes":
            generate_key()  # Generate and save a new key
            print("New encryption key generated and saved.")
            key = load_key()
            print(f"Encryption key loaded: {key}")
            break
        elif choice == "no":
            print("Using existing encryption key.")
            try:
                key = load_key()
                print(f"Encryption key loaded: {key}")
                break
            except FileNotFoundError:
                print("Key file cannot be found, please generate a new encryption key.")
        else:
            print("Please choose yes or no.")
    
    # Prompt user for a message to encrypt
    message = input("Enter the message you want to encrypt: ")
    
    #encrypt the message
    encrypted_message = encrypt_message(message)
    print(f"Encrypted message: {encrypted_message}")
    
    #decrypt the message
    decrypted_message = decrypt_message(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()