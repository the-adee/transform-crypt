# Transform Crypt

**Transform Crypt** is a custom Python encryption system that secures text using a combination of mathematical transformations. It uniquely applies **ASCII-coordinate mapping**, **rotation**, **shear**, and **randomized reflection** to obfuscate characters in a reversible way. A new secret key is generated for each encryption instance and securely stored using Fernet-based symmetric encryption.

---

## Features

- **Coordinate-Based Encryption** – Maps characters to 2D space using ASCII values and their index.
- **Rotation and Shear** – Applies geometric matrix transformations to distort the input.
- **Randomized Reflection** – Reflects every nth character where `n` is randomly chosen per encryption.
- **System-Generated Key** – A new encryption key is created for each encryption instance.
- **Base64 Serialization** – Final encrypted data is encoded for safe transmission or storage.
- **Modular Python Design** – Clean separation of logic across multiple files.

---

## System Workflow

1. Text input is mapped to coordinates.
2. Shear, rotation, and optional reflection transformations are applied.
3. Encrypted coordinates and parameters are serialized.
4. Decryption reverses the process using metadata and key.

---

## Project Structure



```
transform-crypt/
├── main.py                         # Entry point
├── encryption_module/
│   ├── __init__.py                 # Package exports
│   ├── encryption.py               # Encryption logic
│   ├── decryption.py               # Decryption logic
│   ├── transformations.py          # All transformation functions
│   ├── key_manager.py              # Secret key generation and retrieval
│   └── utils.py                    # Base64 encode/decode helpers
```



## Installation & Setup

### Requirements
- Python 3.6 or higher
- No third-party libraries **except**:
  ```bash
  pip install cryptography
  ```

### Clone the Repository
```bash
git clone https://github.com/the-great-adee/transform-crypt.git
cd transform-crypt
```

### Run the Program
```python
python main.py
```

### Example Usage
```python
from encryption_module import encrypt, decrypt

text = "hi how are you"

# encryption
encrypted = encrypt(text)
print("Encrypted:", encrypted)

# cecryption
original = decrypt(encrypted)
print("Decrypted:", original)
```

## Known Limitations

- Floating-point rounding errors may affect very long texts.
- Unicode characters beyond basic multilingual plane (BMP) may not decrypt cleanly.
- No checksum or data integrity validation (can be added in future).
- Key is stored in memory via environment variable during runtime.

## Future Improvements

- Support for full Unicode character set
- Transformation chaining customizability
- File-level encryption support
- GUI for end-users
- Integrity verification (checksums, MACs)
- Improved key storage (external file or encrypted vault)


## License

This project is licensed under the MIT License.


## Contributing

You're welcome to contribute! Feel free to open issues, suggest improvements, or submit pull requests.
