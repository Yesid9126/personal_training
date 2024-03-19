from hashlib import sha256


def get_wompi_signature(reference, amount, currency, integrity_key):
    return sha256(f"{reference}{amount}{currency}{integrity_key}".encode()).hexdigest()
