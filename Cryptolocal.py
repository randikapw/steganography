from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64

# Generate a random 256-bit (32 bytes) AES key
#key = get_random_bytes(32)
#key64= base64.b64encode(key).decode('utf-8')

#Static global key
key64 = "OazOWZVVVBamuaZ9BDkU8lImfu1Nhak0tySQ/zP+CJo="
key = base64.b64decode(key64)

# Encrypt and hash the secret message using a static key
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

    return encrypted_secret, hashed_secret_base64
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

#Hash verification to check integrity
def verify_hash(hash_id, content):
    decoded_content = base64.b64decode(content)
    hashed_secret = hashlib.sha256(decoded_content).digest()

    # Base64 encode the hashed secret for easier storage
    hashed_secret_base64 = base64.b64encode(hashed_secret).decode('utf-8')
    return hash_id == hashed_secret_base64 

def decrypt_stego_image(hashed_secret):

# Initialize AES cipher in ECB mode with the provided key
        cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the secret message
        decrypted_secret = unpad(cipher.decrypt(hashed_secret), AES.block_size)
        return decrypted_secret.decode('utf-8')

def decode_secret(binary_message):
  # Check if the length is divisible by 8 (8 bits per character)
  if len(binary_message) % 8 != 0:
    raise ValueError("Invalid binary message length. Must be divisible by 8.")

  # Split the binary message into 8-bit chunks
  chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

  # Convert each chunk to its corresponding ASCII character
  secret_message = "".join(chr(int(chunk, 2)) for chunk in chunks)

  return secret_message
