import secrets
import string


def generate_secure_password(length=8):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


# Example usage:
secure_password = generate_secure_password()
print(f"Secure Password: {secure_password}")
