from hashlib import sha1, md5
import colorama
from colorama import Fore, Style


# Some decorations for giving it a good look and feel.
colorama.init()
print(Fore.RED + Style.BRIGHT)
print(r"""_________________________________________________________
    __  __          __      ___         __   ___     ___         _                  
   |  \/  |        |  |    /   \       |   \/   |    /   \      | |                    
   | \  / |        |  |   /  __ \      | \   /  |   /  __ \     | |                    
   | |\/| |      _ |  |  /   __  \     | | \/ | |   /  __  \    | |                     
   | |  | |     | |_  |  /  /  \  \    | |    | |  /  /  \  \   | |_______             
   |_|  |_|_____ \___/  /__/   \__\    |_|    |_|  /__/    \__\ |_________|         """)
print("\n****************************************************************")
print()
print(r".______      ___           _______.     _______.____    __    ____  ______   .______       _______  ")
print(r"|   _  \    /   \         /       |    /       |\   \  /  \  /   / /  __  \  |   _  \     |       \ ")
print(r"|  |_)  |  /  ^  \       |   (----`   |   (----` \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  |")
print(r"|   ___/  /  /_\  \       \   \        \   \      \            /  |  |  |  | |      /     |  |  |  |")
print(r"|  |     /  _____  \  .----)   |   .----)   |      \    /\    /   |  `--'  | |  |\  \----.|  '--'  |")
print(r"| _|    /__/     \__\ |_______/    |_______/        \__/  \__/     \______/  | _| `._____||_______/ ")
print(r"                                                                                                    ")
print(r"              ______ .______          ___       ______  __  ___  _______ .______                    ")
print(r"             /      ||   _  \        /   \     /      ||  |/  / |   ____||   _  \                   ")
print(r"            |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |                  ")
print(r"            |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /                   ")
print(r"            |  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.              ")
print(r"             \______|| _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____|              ")
print()

def crack_hash(hash_function, hash_to_crack, file_path):
    with open(file_path, "r") as file:
        for guess in file:
            guess = guess.strip()
            hashed_guess = hash_function(bytes(guess, 'utf-8')).hexdigest()
            if hashed_guess.upper() == hash_to_crack.upper():
                print(f"The password is {guess}")
                return True
            else:
                print(f"Password guess {guess} does not match, trying next...")
    return False

while True:
    # We will determine the type of hash to be cracked
    print()
    print("Enter Type of Hash to be cracked (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit Script")
    print()
    k = input(">")

    if k == "1":
        sha1hash = input("Please input the SHA1 hash to crack.\n>")
        if not crack_hash(sha1, sha1hash, "file.txt"):
            print("Password not in database, we'll get them next time.")

    elif k == "2":
        md5hash = input("Please input the MD5 hash to crack.\n>")
        if not crack_hash(md5, md5hash, "file.txt"):
            print("Password not in database, we'll get them next time.")

    elif k == "3":
        break
