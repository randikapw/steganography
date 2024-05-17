import random
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

possible_zero_width_chars = [
        "\u2060", #WORD JOINER
        "\u200B", #ZERO WIDTH SPACE
        "\u200C", #ZERO WIDTH NON-JOINER
        "\u180E", #MONGOLIAN VOWEL SEPARATOR
        "\u200D", #ZERO WIDTH JOINER
        "\u200E", #LEFT-TO-RIGHT MARK
        "\u200F", #RIGHT-TO-LEFT MARK
        "\uFEFF", #ZERO WIDTH NO-BREAK SPACE
        "\u202A", #LEFT-TO-RIGHT EMBEDDING
        "\u202C", #POP DIRECTIONAL FORMATTING
        "\u202D", #LEFT-TO-RIGHT OVERRIDE
        "\u2062", #INVISIBLE TIMES
        "\u2063"  #INVISIBLE SEPARATOR
]

bin_list = [" ","0","1"]
# char_list = ["\u2060", "\u200B", "\u200C"]
char_list = ["A", "B", "C"]
key = get_random_bytes(32)

# Detect cover text as Sinhala
def detect_sinhala_text(open_text, threshold=0.5):
    try:
        lang_list = detect_langs(open_text)
        for item in lang_list:
            if item.lang == 'si' and item.prob > threshold:
                return True
        return False
    except LangDetectException:
        # Treat short text as Sinhala by default
        return True

# Encrypt and hash the secret message using a random key
def encrypt_and_hash_secret_message(secret_text):
    # Generate a random 256-bit (32 bytes) AES key
    # key = get_random_bytes(32)

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
    
    # return encrypted_secret, hashed_secret_base64, key
    return hashed_secret_base64

#Encode the encrypted secret text in the cover text
def encode(hashed_secret_base64, open_text):
    encoded_text = open_text + "\u2063"
    bin_text = ' '. join(format(ord(x), 'b') for x in hashed_secret_base64)
    print("bin text is:", bin_text)
    # char_list = random.sample(possible_zero_width_chars, len(bin_list))
    for b in bin_text:
        encoded_text += char_list[bin_list.index(b)]
    print("Encoded Text is:", encoded_text)   
    return encoded_text
#Decode the stego text when the user enters it. This should be stored in the variable stego_text
def decode(stego_text):
	bin_text = ""
	for w in open_text:
		if w in char_list:
			bin_text += bin_list[char_list.index(w)]
	bin_val = bin_text.split()
	secret_text = ""
	for b in bin_val:
		secret_text += chr(int(b, 2))
	return secret_text
#Decrypt the decoded hashed stego text to get the secret text. How to get the key???
def decrypt_stego_text(secret_text, key):
        #base64 decode the encoded secret
        hashed_secret = base64.b64decode(secret_text)
        # Initialize AES cipher in ECB mode with the provided key
        cipher = AES.new(key, AES.MODE_ECB)
        # Decrypt the secret message
        decrypted_secret = unpad(cipher.decrypt(hashed_secret), AES.block_size)
        return decrypted_secret.decode('utf-8')

def main():
    print("Welcome to Sinhala Steganography!")
    while True:
# Ask the user to enter the cover text in Sinhala
        open_text = input("Enter the cover text in Sinhala: ")
        
        # Check if the cover text is in Sinhala
        try:
            if detect_sinhala_text(open_text):
                print("Sinhala text detected!")
                break
        except LangDetectException:
            print("An error occurred while detecting the language of the cover text. Please try again.")
            continue 
    secret_text = input("Enter the secret message to hide: ")

    steganographed_text = encode(encrypt_and_hash_secret_message(secret_text), open_text) 
        
  # Print the steganographed text
    print("Steganographed text:", steganographed_text)
        
#Decoding
#Input the stego text
    print("Enter the steganographed text: ")
    separator_index = steganographed_text.rfind("\u2063")
    stego_text = steganographed_text[separator_index + 1:]
     
    output_secret = decrypt_stego_text(decode(stego_text), key)

#Print the decoded and decrypted secret
    print("Decoded Secret: ", output_secret)

if __name__ == "__main__":
  main()



