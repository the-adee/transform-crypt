from encryption_module.encryption import encrypt
from encryption_module.decryption import decrypt
import time

execution_start_time = time.time()

if __name__ == "__main__":
    text = "hi how you em@il"
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

    encryption_execution_start_time = time.time()

    # Encrypt
    encrypted_data = encrypt(text)
    print("🔐 Encrypted Data:", encrypted_data)

    encryption_execution_end_time = time.time()
    print(encryption_execution_end_time - encryption_execution_start_time)


    decryption_execution_start_time = time.time()

    # Decrypt
    decrypted_text = decrypt(encrypted_data)
    print("🔓 Decrypted Text:", decrypted_text)

    decryption_execution_end_time = time.time()
    
    print(decryption_execution_end_time - decryption_execution_start_time)

execution_end_time = time.time()


print(execution_end_time - execution_start_time)
