import math

def apply_shear(coords, s_x, s_y):
    """Applies shear transformation."""
    return [(x + s_x * y, y + s_y * x) for x, y in coords]

def reverse_shear(coords, s_x, s_y):
    """Reverses shear transformation."""
    return [((x - s_x * y) / (1 - s_x * s_y), (y - s_y * x) / (1 - s_x * s_y)) for x, y in coords]

def apply_rotation(coords, angle):
    """Applies rotation transformation."""
    theta = math.radians(angle)
    cos_theta, sin_theta = math.cos(theta), math.sin(theta)
    return [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for x, y in coords]

def reverse_rotation(coords, angle):
    """Reverses rotation transformation."""
    theta = math.radians(-angle)
    cos_theta, sin_theta = math.cos(theta), math.sin(theta)
    return [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for x, y in coords]

def apply_reflection(coords, reflection_n):
    """Applies reflection on every nth character."""
    return [(x, -y) if (i + 1) % reflection_n == 0 else (x, y) for i, (x, y) in enumerate(coords)]

def reverse_reflection(coords, reflection_n):
    """Reverses reflection on every nth character."""
    return [(x, -y) if (i + 1) % reflection_n == 0 else (x, y) for i, (x, y) in enumerate(coords)]
