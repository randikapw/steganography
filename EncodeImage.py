from Cryptolocal import encrypt_and_hash_secret_message
from PIL import Image
import os

def encode_image():
    #Get the current working directory
    cwd = os.getcwd()
    print (f"The Current Working Directory is :{cwd}")
    print()

    #Ask the path to the  cover image from the user
    image_path = input("Enter the Cover Image Path: ")
    print()

    #Validating the Image Path
    try:
        #Load the Stego Image
        img = Image.open(image_path)
        pixels = img.load()

        #Input the secret text
        secret_text = input("Enter the Secret Message to hide :")
        print()

        #Encrypt the secret
        encrypted_secret, hashed_secret_base64= encrypt_and_hash_secret_message(secret_text)
        #print("Encrypted Secret: ", encrypted_secret)

        # Convert the secret message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in encrypted_secret)
        #print("Binary Message: ", binary_message)

        # Add a delimiter to mark the end of the message
        binary_message += '1111111111111110'  # Delimiter to signify end of message
        #print("Binary with Delimiter: ", binary_message)

        #Initialize variables
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

        #Input the output image path
        output_image_path = input("Enter the Output Image Path: ")
        print()

        #Save the output image
        img.save(output_image_path)

        #Save the Hash ID in a file and save in the same location as the image
        with open(output_image_path + ".h", "w") as hashfile:
            hashfile.write(hashed_secret_base64)
        
        #Print the Output file location
        print("Secret message encoded and saved to: ", output_image_path)
        pass
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}!!!")
