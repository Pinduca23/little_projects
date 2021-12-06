import secrets
import string
import json
import os
import pyperclip as pc


def pass_size():
    # Gets desired password length
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
    # Getting where the password is from
    user_log = input('What is this password for?: ').upper()
    return(user_log)


# Declaring user dict
user = {}


def xkcd_password():
    # Creating XKCD passwords made up of word list from .txt
    with open(file='D:\PyProjectLuis\little_projects\wpa2-wordlists\PlainText\words.txt') as o:
        words = [word.strip() for word in o]
        password = ' '.join(secrets.choice(words)
                            for i in range(pass_size())).title()
    print(password)
    user = {where_from(): password}
    write_pass(user)
    clear()


def alphanumeric_pass():
    # Creating passwords from numbers/letters/symbols
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
    write_pass(user)
    clear()


def get_password():
    # Function to get passwords
    data_from = input('Which password would you like to see? \n').upper()
    data = read_pass()
    password = data.get(data_from)
    if password == None:
        print('Password for that login doesn''t exist')
    else:
        print('The password for', data_from.title(),
              'is:', password)
        print('Password copied to clipboard!')
        pc.copy(password)
        clear()


# JSON file path where passwords area stored.
passwords_path = 'D:\PyProjectLuis\little_projects\PassPy\passwords.json'


def write_pass(user):
    # Function designed to write passwords.json
    with open(passwords_path, 'r+', encoding='utf-8') as f:
        try:
            data = json.load(f)
            data.update(user)
            f.seek(0)
            json.dump(data, f, ensure_ascii=True, indent=4)
        except:
            json.dump(user, f, ensure_ascii=True, indent=4)
    f.close()


def read_pass():
    # Function to read passwords.json
    f = open(passwords_path, 'r')
    data = json.loads(f.read())
    f.close()
    return data


def clear():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
