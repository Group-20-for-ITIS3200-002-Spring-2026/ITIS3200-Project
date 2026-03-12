# pip3 install pycryptodome for AES encryption,
# padding, SHA256, and MAC verification

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256, HMAC

# Generates Public Key of User 1 and User 2
def generate_public_key(private_key, g, p):
    return pow(g,private_key,p)

# Generates Shared Key of User 1 and User 2
def generate_shared_key(other_user_public_key, private_key, p):
    return pow(other_user_public_key, private_key, p)

# Deriving the key needed for encryption
def derive_key(shared_key):
    h = SHA256.new()
    h.update(str(shared_key).encode())
    return h.digest()

# Encryptes the text
def encrypt_text(message, key):
    cipher = AES.new(key,AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext



