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
from Config import *

#Decode the stego text when the user enters it. This should be stored in the variable stego_text
def decode():
    #Input the stego text
    file_name = input("Enter the filename of steganographed text: ")
    with open(file_name, "r") as file:
    # Read the entire content of the file into a string
        stego_text = file.read()
    print("Stego Text:", stego_text)
    separator_index = stego_text.rfind("\u2063")
    raw_secret = stego_text[separator_index + 1:]
    print("Raw Secret:", raw_secret)
    bin_text = ""
    for w in raw_secret:
        if w in char_list:
            bin_text += bin_list[char_list.index(w)]
    print("Bin Text:", bin_text)
    bin_val = bin_text.split()
    secret_text = ""
    for b in bin_val:
        secret_text += chr(int(b, 2))
    print("Secret Text: ", secret_text)
    output_secret = decrypt_stego_text(secret_text)
    print("Display Secret: ", output_secret)

    

