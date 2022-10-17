### Password Manager

from functions import pw_entry, display, load_key
from cryptography.fernet import Fernet

UserPWD = input('Enter Password to Access: ')
MasterPWD = "Hello"
key = load_key() + MasterPWD.encode()
user_key = load_key() + UserPWD.encode()
fer = Fernet(key)


if user_key == key :
    while True:
        mode = input("Please select the mode you would like to use:   add    view    exit" '\n' " :").lower()
        if mode == 'exit':
            break
        elif mode == 'add':
            pw_entry(fer)
        elif mode == 'view':
            display(fer)
        else:
            print("Invalid Input")
            continue
