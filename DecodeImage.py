from Cryptolocal import decrypt_stego_text, decode_secret, verify_hash
from PIL import Image
import os

def decode_image():
  #Get the current working directory
  cwd = os.getcwd()
  print (f"The Current Working Directory is :{cwd}")
  print()

  # Get image path from user
  stego_image_path = input("Enter the Stego Image Path: ")
  print()
  
  try:
    #Load the Image
    img = Image.open(stego_image_path)
    pixels = img.load()

    # Initialize variables
    binary_message = ""
    delimiter = '1111111111111110'  # Same delimiter used for encoding
    delimiter_found = False

    #Iterate through each pixel
    for y in range(img.height):
      for x in range(img.width):
        # Extract the least significant bit from each color channel
        for i in range(3):  # Iterate over RGB channels
          pixel = pixels[x, y][i]
          binary_message += str(pixel & 1)

          #Check if delimiter is reached
          index = binary_message.find(delimiter)
          if index != -1:
              binary_message = binary_message[:index]
              delimiter_found = True
              #print("Binary Message: ", binary_message)
              break
        if delimiter_found:
           break
      if delimiter_found:
         break 
    #print("Binary Message Final: ", binary_message)

    #Convert binary message to bytes
    byte_array = bytearray()
    for i in range(0, len(binary_message), 8):
      byte = binary_message[i:i+8]
      byte_array.append(int(byte, 2))
    #print("Byte Array: ", byte_array)

    secret_text = decode_secret(binary_message)
    #print("Secret Text: ", secret_text)

    #Read the hash ID from file
    try:
        with open(stego_image_path + ".h", "r") as hashfile:
            hash_id = hashfile.read()
            #print("Hash ID is: ", hash_id)
    except FileNotFoundError:
        print("Hash File Not Found!!!")
        return

    #Verify Hash and decrypt the secret
    if verify_hash(hash_id, byte_array):
        try:
            output_secret = decrypt_stego_text(secret_text)
            print("Secret Message: ", output_secret)
        except:
            print("Error during decryption!!!")
    else:
        print("Error in Hash ID Verification!!!")

  except FileNotFoundError:
     print(f"Error: Image not found at {stego_image_path}!!!")

