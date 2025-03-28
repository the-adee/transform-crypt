from encryption_module.encryption import encrypt
from encryption_module.decryption import decrypt

if __name__ == "__main__":
    text = "hi how are you"
    sample_text = """Odds are that he is cheating on her.
    I’m on the fence.
    He's got the biggest eyebrows I've ever seen.
    She’s now wearing headphones.
    We put you on probation.
    It’s as quick as lightning.
    Philosophy was great until the nerds took over and started putting math symbols every other sentence just to try to sound smart.
    She decided to take the bus because it was supposed to be quicker, but then it ended up being twenty minutes late.
    Stand up straight!
    Never do that again!"""

    # Encrypt
    encrypted_data = encrypt(text)
    print("🔐 Encrypted Data:", encrypted_data)

    # Decrypt
    decrypted_text = decrypt(encrypted_data)
    print("🔓 Decrypted Text:", decrypted_text)
