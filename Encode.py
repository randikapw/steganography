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

from Cryptolocal import *
from Langcheck import *
from Config import *

#Encode the encrypted secret text in the cover text
def encode():
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
    encrypted_secret, hashed_secret_base64, key = encrypt_and_hash_secret_message(secret_text)
    print("encrypted secret: ", encrypted_secret)
    encoded_text = open_text + "\u2063"
    bin_text = ' '. join(format(ord(x), 'b') for x in hashed_secret_base64)
    print("bin text is:", bin_text)
    # char_list = random.sample(possible_zero_width_chars, len(bin_list))
    for b in bin_text:
        encoded_text += char_list[bin_list.index(b)]
    file_name = input("Enter the filename to save the steganographed text: ")
    with open(file_name, "w") as file:
    # Write the content of the variable to the file
        file.write(encoded_text)
    print("The encoded text was successfully saved to the file:", file_name)
