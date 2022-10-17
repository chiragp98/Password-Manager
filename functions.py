from cryptography.fernet import Fernet


def display(fer):
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            sitename, user, pwd = data.split('|')
            print('Site: ' + sitename,' User: '  + user, ' Password: ' + str(fer.decrypt(pwd[1:])),'\n')


def pw_entry(fer):
    Site = input('Site Name: ')
    Username = input('Username: ')
    Password = input('Password: ')

    with open ('passwords.txt', 'a') as f:
        f.write(Site + '|' + Username + '|' + str(fer.encrypt(Password.encode())) + '\n')

### Function to create key 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''
## load key for master pw
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

