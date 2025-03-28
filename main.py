from encryption_module.encryption import encrypt
from encryption_module.decryption import decrypt

if __name__ == "__main__":
    text = "hi how are you"

    # Encrypt
    encrypted_data = encrypt(text)
    print("🔐 Encrypted Data:", encrypted_data)

    # Decrypt
    decrypted_text = decrypt(encrypted_data)
    print("🔓 Decrypted Text:", decrypted_text)
