### Password Manager
from functions import pw_entry, display

MasterPWD = input("Master Password: ")


while True:
    mode = input("Please select the mode you would like to use:   add    view    exit" '\n' " :").lower()
    if mode == 'exit':
        break
    elif mode == 'add':
        pw_entry()
    elif mode == 'view':
        display()
    else:
        print("Invalid Input")
        continue





