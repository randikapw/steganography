from Decode import decode
from Encode import encode
from Banner import *
from EncodeImage import encode_image
from DecodeImage import decode_image

def select_cover():
    #Select the Cover Type
    print("Choose the desired cover:")
    print()
    print(f"{'1. Sinhala Text Cover':>30}")
    print()
    print(f"{'2. Image Cover':>23}")
    print()

    #Ask the user to input the Technique
    choice = input("Enter the Cover Type (1 or 2):")
    print()
    if choice == '1':
        print(f"{'!!!! You have chosen Sinhala Text Cover !!!!':>53}")
        print()
        if is_need_to_encode():
            encode()

        else:
            decode()

    elif choice == '2':
        print(f"{'!!!! You have chosen Image Cover !!!':>45}")
        print()
        if is_need_to_encode_2():
            encode_image()
        else:
            decode_image()
    else:
        print("Invalid Choice!!")

#For Text Cover
def is_need_to_encode():
    #Select the Technique
    print("Choose the Technique (1 or 2): ")
    print()
    print(f"{'1. Encode':>18}")
    print()
    print(f"{'2. Decode':>18}")
    print()

    #Ask the user to enter the choice
    action = input("Choose the Technique (1 or 2): ")
    print()

    if action.upper() in ("1", "2"):
        if action.upper() == "1":
            return True
        else:
            return False
    else:
        print("!! Invalid action provided. Please Try Again !!") 
    

#For Image Cover
def is_need_to_encode_2():
    #Select the Technique
    print("Choose the Technique (1 or 2): ")
    print()
    print(f"{'1. Encode':>18}")
    print()
    print(f"{'2. Decode':>18}")
    print()

    #Ask the user to enter the choice
    action = input("Choose the Technique (1 or 2): ")
    print()

    if action.upper() in ("1", "2"):
        if action.upper() == "1":
            return True
        else:
            return False
    else:
        print("!! Invalid action provided. Please Try Again !!") 
    

def main():
    print_banner()
    select_cover()

if __name__ == "__main__":
  main()
    
