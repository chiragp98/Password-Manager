def display():
    pass

def pw_entry():
    Username = input('Username: ')
    Password = input('Password: ')

    with open ('passwords.txt', 'a') as f:
        f.write(Username + " | " + Password + '\n')