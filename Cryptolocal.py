from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
import nltk
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import base64
nltk.download('punkt')

# Generate a random 256-bit (32 bytes) AES key
#key = get_random_bytes(32)
#key64= base64.b64encode(key).decode('utf-8')
key64 = "OazOWZVVVBamuaZ9BDkU8lImfu1Nhak0tySQ/zP+CJo="
key = base64.b64decode(key64)


# Encrypt and hash the secret message using a random key
def encrypt_and_hash_secret_message(secret_text):

    # Initialize AES cipher in ECB mode with the generated key
    cipher = AES.new(key, AES.MODE_ECB)

    # Convert the secret message to bytes
    secret_bytes = secret_text.encode('utf-8')

    # Encrypt the secret message with AES-256
    encrypted_secret = cipher.encrypt(pad(secret_bytes, AES.block_size))

    # Hash the encrypted secret with SHA-256
    hashed_secret = hashlib.sha256(encrypted_secret).digest()

    # Base64 encode the hashed secret for easier storage
    hashed_secret_base64 = base64.b64encode(hashed_secret).decode('utf-8')
    encrypted_secret = base64.b64encode(encrypted_secret).decode('utf-8')

    return encrypted_secret, hashed_secret_base64, key
    # return hashed_secret_base64

#Decrypt the decoded hashed stego text to get the secret text. How to get the key???
def decrypt_stego_text(secret_text):
        #base64 decode the encoded secret
        hashed_secret = base64.b64decode(secret_text)
        # Initialize AES cipher in ECB mode with the provided key
        cipher = AES.new(key, AES.MODE_ECB)
        # Decrypt the secret message
        decrypted_secret = unpad(cipher.decrypt(hashed_secret), AES.block_size)
        return decrypted_secret.decode('utf-8')
