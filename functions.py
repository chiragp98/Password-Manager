def display():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            sitename, user, pwd = data.split('|')
            print('Site: ' + sitename,' User: '  + user, ' Password: ' + pwd,'\n')


def pw_entry():
    Site = input('Site Name: ')
    Username = input('Username: ')
    Password = input('Password: ')

    with open ('passwords.txt', 'a') as f:
        f.write(Site + '|' + Username + '|' + Password + '\n')