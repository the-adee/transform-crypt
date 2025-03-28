from encryption_module.key_manager import get_secret_key
from encryption_module.transformations import reverse_shear, reverse_rotation, reverse_reflection
from encryption_module.utils import decode_coordinates

def decrypt(encrypted_data):
    """Decrypts text using the stored secret key."""
    secret_key = get_secret_key()

    # Extract metadata and encrypted coordinates
    metadata, encrypted_text = encrypted_data.split("|", 4)[0:4], encrypted_data.split("|", 4)[-1]
    angle, s_x, s_y, reflection_n = map(float, metadata)
    reflection_n = int(reflection_n)

    # Decode coordinates
    encrypted_coords = decode_coordinates(encrypted_text)

    # Reverse transformations
    reflected_coords = reverse_reflection(encrypted_coords, reflection_n)
    rotated_coords = reverse_rotation(reflected_coords, angle)
    original_coords = reverse_shear(rotated_coords, s_x, s_y)

    # Convert back to text
    decrypted_text = ''.join(chr(round(x)) for x, _ in original_coords)
    return decrypted_text
