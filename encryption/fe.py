import base64

# Secret key (can be shared securely later)
SECRET_KEY = "fe-key-123"


def encrypt(value):
    """
    Simulated encryption using base64
    """
    value_str = str(value)
    encoded = base64.b64encode(value_str.encode()).decode()
    return encoded


def decrypt(encoded_value, key):
    """
    Controlled decryption with key-based access
    """
    print("[FE] Decryption requested")

    if key != SECRET_KEY:
        print("[FE] Unauthorized access attempt")
        raise PermissionError("Unauthorized access")

    print("[FE] Access granted")

    decoded = base64.b64decode(encoded_value.encode()).decode()
    return float(decoded)


def decrypt_role(role, encoded_value, key):
    """
    Role-based access control
    Example: Manager data is restricted
    """
    if role == "Manager" and key != SECRET_KEY:
        raise PermissionError("Access denied for Manager data")

    return decrypt(encoded_value, key)
