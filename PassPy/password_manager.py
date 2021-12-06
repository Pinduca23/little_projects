import secrets
import string
import json


pass_length = 0
while True:
    try:
        pass_length = int(input('Required size of password: '))
        if pass_length <= 3:
            print('Password must have at least 4 characters or words')
        else:
            break
    except:
        print('Not a valid number')


def xkcd_password():
    with open(file='D:\PyProjectLuis\little_projects\wpa2-wordlists\PlainText\words.txt') as o:
        words = [word.strip() for word in o]
        password = ' '.join(secrets.choice(words)
                            for i in range(pass_length)).title()
        print(password)


def alphanumeric_pass():
    while True:
        everything = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(secrets.choice(everything)
                           for i in range(pass_length))
        if (any(c.islower() for c in password)
            and (c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1):
            break
    print(password)