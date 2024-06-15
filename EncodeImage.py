from Cryptolocal import encrypt_and_hash_secret_message
from PIL import Image

def encode_image():
    #Ask the path to the  cover image from the user
    image_path = input("Enter the Cover Image Name: ")
    img = Image.open(image_path)
    pixels = img.load()
    secret_text = input("Enter the Secret Message to hide :")
    encrypted_secret, hashed_secret_base64= encrypt_and_hash_secret_message(secret_text)
    #print("Encrypted Secret: ", encrypted_secret)
    # Convert the secret message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_secret)
    #print("Binary Message: ", binary_message)
    # Add a delimiter to mark the end of the message
    binary_message += '1111111111111110'  # Delimiter to signify end of message
    #print("Binary with Delimiter: ", binary_message)
    # Initialize variables
    message_index = 0
    message_length = len(binary_message)
    # Iterate through each pixel in the image
    for y in range(img.height):
        for x in range(img.width):
            if message_index < message_length:
                # Get the pixel value (R, G, B)
                pixel = list(pixels[x, y])
                # Modify the least significant bit of each color channel
                for i in range(3):  # Iterate over RGB channels
                    if message_index < message_length:
                        pixel[i] = (pixel[i] & ~1) | int(binary_message[message_index])
                        message_index += 1
                # Update the pixel with the modified value
                pixels[x, y] = tuple(pixel)
    output_image_Name = input("Enter the Output Image Name: ")
    # Save the output image
    img.save(output_image_Name)
    #hash_filename = input("Enter Hash File Name: ")
    #with open(hash_filename + ".h", "w") as hashfile:
        #hashfile.write(hashed_secret_base64)
    print("Secret message encoded and saved to: ", output_image_Name)
