from langdetect.lang_detect_exception import LangDetectException
from Cryptolocal import encrypt_and_hash_secret_message
from Langcheck import detect_sinhala_text
from Config import bin_list,char_list
import os

#Encode the encrypted secret text in the cover text
def encode():
    while True:
          #Get the current working directory
          cwd = os.getcwd()
          print (f"The Current Working Directory is :{cwd}")
          print()

          #Ask the user to enter the cover text in Sinhala
          open_text = input("Enter the cover text in Sinhala: ")
          print()

          #Check if the cover text is in Sinhala
          try:
              if detect_sinhala_text(open_text):
                  print("Sinhala text detected!")
                  print()
                  break
          except LangDetectException:
              print("An error occurred while detecting the language of the cover text. Please try again.")
              print()
              continue
    #Enter the secret message to be encoded
    secret_text = input("Enter the secret message to hide: ")
    print()

    #Encrypt the secret message and obtain the hashID
    encrypted_secret, hashed_secret_base64 = encrypt_and_hash_secret_message(secret_text)

    #Encode the secret message
    encoded_text = open_text + "\u2063"
    bin_text = ' '. join(format(ord(x), 'b') for x in encrypted_secret)
    for b in bin_text:
        encoded_text += char_list[bin_list.index(b)]

    #Enter a filename to save the output
    file_path = input("Enter the Output Text File Path: ")
    print()

    #Write the stego text and hash ID to two files
    with open(file_path + ".txt", "w") as file:
        file.write(encoded_text)
    with open(file_path + ".h", "w") as hashfile:
        hashfile.write(hashed_secret_base64)

    #Print the output filename
    print("The encoded text was successfully saved to the file:", file_path)
