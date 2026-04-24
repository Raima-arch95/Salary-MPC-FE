import base64

def encrypt(value):
    """
    Simulated encryption: encode value as base64 string
    """
    value_str = str(value)
    encoded = base64.b64encode(value_str.encode()).decode()
    return encoded


def decrypt(encoded_value):
    """
    Simulated decryption: decode base64 string
    """
    decoded = base64.b64decode(encoded_value.encode()).decode()
    return float(decoded)
