from Decode import decode
from Encode import encode

def is_need_to_encode():
    while True:
    # Ask the user to selct either Encode option or Decode option
        action = input("What do you want to do now? encode a text (E) or decode a text (D) ")
        if action.upper() in ("E", "D"):
            if action.upper() == "E":
                return True
            else:
                return False
        else:
            print("Invalid action provided. Only supports E or D")

def main():
    print("Welcome to !!!STEALTHSCRIPT!!!ල")
    if is_need_to_encode():
        encode()
    
    else:
        decode()

if __name__ == "__main__":
  main()
    
