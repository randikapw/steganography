from Decode import decode
from Encode import encode
from Banner import *
from EncodeImage import encode_image
from DecodeImage import decode_image

def select_cover():
    print("Choose the desired cover:")
    print("1. Sinhala Text Cover")
    print("2. Image Cover")

    #Ask the user to input the choice
    choice = input("Enter the choice (1 or 2):")
    if choice == '1':
        print("You have chosen Sinhala Text Cover")
        if is_need_to_encode():
            encode()

        else:
            decode()

    elif choice == '2':
        print("You have chosen Image Cover")
        if is_need_to_encode_2():
            encode_image()
        else:
            decode_image()
    else:
        print("Invalid Choice!!")

#For Text Cover
def is_need_to_encode():
    while True:
    # Ask the user to enter the choice
        action = input("What do you want to do now? encode a text (E) or decode a text (D) ")
        if action.upper() in ("E", "D"):
            if action.upper() == "E":
                return True
            else:
                return False
        else:
            print("Invalid action provided. Only supports E or D")

#For Image Cover
def is_need_to_encode_2():
    while True:
    # Ask the user to enter the choice
        action = input("What do you want to do now? encode a text (E) or decode a text (D) ")
        if action.upper() in ("E", "D"):
            if action.upper() == "E":
                return True
            else:
                return False
        else:
            print("Invalid action provided. Only supports E or D")

def main():
    print_banner()
    select_cover()

if __name__ == "__main__":
  main()
    
