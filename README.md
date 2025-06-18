# Rotational Encryption System

This project implements a **custom encryption and decryption system in Python** that secures text data using a combination of mathematical transformations. It uses **ASCII-coordinate mapping**, **rotation**, **shear**, and **randomized reflection** transformations to produce a reversible encrypted form of text. A secret key, generated randomly each time, is used to drive these transformations and is securely stored using symmetric encryption (`Fernet`).

---

## Features

- **Coordinate-based encryption**: Maps characters to 2D space using ASCII and index.
- **Rotation and Shear**: Applies matrix-based geometric transformations.
- **Random Reflection**: Reflects every nth character where `n` is randomly generated.
- **System-Generated Key**: A unique encryption key is generated per instance.
- **Base64 Serialization**: Encoded encrypted data is safely transmitted as a single string.
- **Modular Design**: Each module is separated logically for readability and reuse.

---

## System Workflow

1. **Text input** is converted to coordinate pairs.
2. **Transformations** are applied in the order: Shear → Rotation → Reflection.
3. All data is **serialized** and returned as an encrypted string.
4. During decryption, the steps are reversed using metadata from the encrypted string.

## Project Structure

```
rotational-encryption/
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
git clone https://github.com/your-username/rotational-encryption.git
cd rotational-encryption
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

Feel free to submit issues, suggest features, or create pull requests.
