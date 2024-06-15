from Cryptolocal import decrypt_stego_text, verify_hash
from Config import bin_list,char_list

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


def decode():
    #Decoding
#Input the stego text
    file_name = input("Enter the filename of steganographed text: ")
    try:
        with open(file_name + ".txt", "r") as file:
        # Read the entire content of the file into a string
            stego_text = file.read()
        separator_index = stego_text.rfind("\u2063")
        raw_secret = stego_text[separator_index + 1:]
        decoded_secret = decodex(raw_secret)
        try:
            with open(file_name + ".h", "r") as hashfile:
                hash_id = hashfile.read()
            if verify_hash(hash_id, decoded_secret):
                output_secret = decrypt_stego_text(decoded_secret)

            #Print the decoded and decrypted secret
                print("Decoded Secret: ", output_secret)
            else:
                print("Error in Hash ID Verification!")
        except FileNotFoundError:
            print("Hash File Not Found!")
    except FileNotFoundError:
        print(file_name + ".txt File Not Found!")

