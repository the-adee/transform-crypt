import base64

def encode_coordinates(coords):
    """Encodes coordinate list to Base64 string."""
    return base64.b64encode(str(coords).encode()).decode()

def decode_coordinates(encoded_str):
    """Decodes Base64 string back to coordinate list."""
    return eval(base64.b64decode(encoded_str).decode())  # Convert string back to list
