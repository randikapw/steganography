from Cryptolocal import decrypt_stego_text, verify_hash
from Config import bin_list,char_list
import os

#Decode the encrypted secret from the cover text
def decodex(raw_secret):
    bin_text = ""
    for w in raw_secret:
        if w in char_list:
            bin_text += bin_list[char_list.index(w)]
    bin_val = bin_text.split()
    secret_text = ""
    for b in bin_val:
        secret_text += chr(int(b, 2))
    #print("Secret Text: ", secret_text)
    return secret_text

#Actual decoding rpocess begins from here
def decode():
    #Get the current working directory
    cwd = os.getcwd()
    print (f"The Current Working Directory is :{cwd}")
    print()

    #Input the stego text
    file_path = input("Enter the Stego File Path: ")
    print()

    #Read the file and decrypt the secret
    try:
        with open(file_path + ".txt", "r", encoding="utf-8") as file:
            #Read the entire content of the file into a string
            stego_text = file.read()
        separator_index = stego_text.rfind("\u2063")

        #Extract the raw secret
        raw_secret = stego_text[separator_index + 1:]

        #Decode the raw secret from the function above
        decoded_secret = decodex(raw_secret)
        try:
            with open(file_path + ".h", "r") as hashfile:
                hash_id = hashfile.read()

            #Perform Hash ID verification
            if verify_hash(hash_id, decoded_secret):
                output_secret = decrypt_stego_text(decoded_secret)

                #Print the decoded and decrypted secret
                print("Decoded Secret: ", output_secret)
            else:
                print("Error in Hash ID Verification!")
        except FileNotFoundError:
            print("Hash File Not Found!")
    except FileNotFoundError:
        print(file_path + ".txt File Not Found!")

