from Cryptolocal import decrypt_stego_text
from PIL import Image

def decode_image():
  """Decodes a secret message hidden in an image."""

  # Get image path from user
  stego_image_path = input("Enter the Stego Image Path: ")
  #hash_filename = input("Enter Hash File Name: ")

  # Load the image
  img = Image.open(stego_image_path)
  pixels = img.load()

  # Initialize variables
  binary_message = ""
  delimiter = '1111111111111110'  # Same delimiter used for encoding

  # Iterate through each pixel
  for y in range(img.height):
    for x in range(img.width):
      # Extract the least significant bit from each color channel
      for i in range(3):  # Iterate over RGB channels
        pixel = pixels[x, y][i]
        binary_message += str(pixel & 1)

      # Check if delimiter is reached
      if binary_message[-len(delimiter):] == delimiter:
        # Remove the delimiter
        binary_message = binary_message[:-len(delimiter)]
        #print("Binary Message: ", binary_message)
        break
  #print("Binary Message: ", binary_message)

  # Convert binary message to bytes
  byte_array = bytearray()
  for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i+8]
    byte_array.append(int(byte, 2))
  #print("Secret Text: ", secret_text)

  #Read the hash ID from file
  #try:
      #with open(hash_filename+ ".h", "r") as hashfile:
          #hash_id = hashfile.read()
          #print("Hash ID is: ", hash_id)
  #except FileNotFoundError:
      #print("Hash File Not Found!!!")
      #return

  #Verify Hash
  #if verify_hash(hash_id, byte_array):
      #try:
          #output_secret = decrypt_stego_text(byte_array)
          #print("Secret Message: ", output_secret)
      #except:
          #print("Error during decryption!!!")
  #else:
      #print("Error in Hash ID Verification!!!")


  # Decrypt the message
  try:
      output_secret = decrypt_stego_text(secret_text)
      print("Secret Message: ", output_secret)
  except:
      print("Error during decryption!")


