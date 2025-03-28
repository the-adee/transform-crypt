import hashlib
import random
from encryption_module.key_manager import get_secret_key
from encryption_module.transformations import apply_shear, apply_rotation, apply_reflection
from encryption_module.utils import encode_coordinates

def encrypt(text):
    """Encrypts text using matrix transformations and randomized reflection."""
    secret_key = get_secret_key()

    # Generate transformation values from key
    key_hash = hashlib.sha256(secret_key.encode()).hexdigest()
    angle = int(key_hash[:2], 16) % 90
    s_x = (int(key_hash[2:4], 16) % 10) / 10
    s_y = (int(key_hash[4:6], 16) % 10) / 10
    reflection_n = random.randint(50, 150)

    # Convert text to coordinates
    coordinates = [(ord(char), i + 1) for i, char in enumerate(text)]

    # Apply transformations
    sheared_coords = apply_shear(coordinates, s_x, s_y)
    rotated_coords = apply_rotation(sheared_coords, angle)
    encrypted_coords = apply_reflection(rotated_coords, reflection_n)

    # Encode and return encrypted data
    metadata = f"{angle}|{s_x}|{s_y}|{reflection_n}"
    encrypted_text = encode_coordinates(encrypted_coords)
    return f"{metadata}|{encrypted_text}"
