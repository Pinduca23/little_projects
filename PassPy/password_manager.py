import secrets
import string
import json


def pass_size():
    pass_length = 0
    while True:
        try:
            pass_length = int(input('Required size of password: '))
            if pass_length <= 3:
                print('Password must have at least 4 characters or words')
            else:
                return(pass_length)
        except:
            print('Not a valid number')


def where_from():
    user_log = input('What is this password for?: ').upper()
    return(user_log)


user = {}


def xkcd_password():
    with open(file='D:\PyProjectLuis\little_projects\wpa2-wordlists\PlainText\words.txt') as o:
        words = [word.strip() for word in o]
        password = ' '.join(secrets.choice(words)
                            for i in range(pass_size())).title()
    print(password)
    user = {where_from(): password}
    stored_pass(user, mode = 'a')


def alphanumeric_pass():
    while True:
        everything = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(secrets.choice(everything)
                           for i in range(pass_size()))
        if (any(c.islower() for c in password)
            and (c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1):
            break
    user = {where_from(): password}
    print(password)
    stored_pass(user,mode = 'a')


def stored_pass(user, mode):
    file_path = 'D:\PyProjectLuis\little_projects\PassPy\passwords.json'
    with open(file_path, mode , encoding='utf-8') as f:
        json.dump(user, f, ensure_ascii=True, indent=4)
