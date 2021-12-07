import secrets
import string
import json
import os
import pyperclip as pc


def pass_size():
    # Gets desired password length
    while True:
        try:
            pass_length = int(input('\nRequired size of password: '))
            if pass_length <= 3:
                print('\nPassword must have at least 4 characters or words')
            else:
                return(pass_length)
        except ValueError:
            print('\nNot a valid number')


def where_from():
    # Getting where the password is from
    user_log = input('\nWhat is this password for?: ').upper()
    return(user_log)


# Declaring user dict
user = {}


def xkcd_password():
    # Creating XKCD passwords made up of word list from .txt
    length = pass_size()
    with open(file='PassPy\words.txt') as o:
        words = [word.strip() for word in o]
        password = ' '.join(secrets.choice(words)
                            for i in range(length)).title()
    user = {where_from(): password}
    clear()
    print('\nYour new XKCD password:', password)
    write_pass(user)


def alphanumeric_pass():
    # Creating passwords from numbers/letters/symbols
    length = pass_size()
    while True:
        everything = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(secrets.choice(everything)
                           for i in range(length))
        if (any(c.islower() for c in password)
            and (c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    user = {where_from(): password}
    clear()
    print('\nYour new password:', password)
    write_pass(user)


def get_password():
    # Function to get passwords
    data_from = input('Which password would you like to see? \n').upper()
    data = read_pass()
    password = data.get(data_from)
    if password == None:
        print('\nPassword for that login doesn''t exist')
    else:
        clear()
        print('\nThe password for', data_from.title(),
              'is:', password)
        print('\nPassword copied to clipboard!')
        pc.copy(password)


# JSON file path where passwords area stored.
passwords_path = 'PassPy\passwords.json'


def write_pass(user):
    # Function designed to write passwords.json
    try:
        with open(passwords_path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.update(user)
            f.seek(0)
            json.dump(data, f, ensure_ascii=True, indent=4)
        f.close()
    except FileNotFoundError:
        with open(passwords_path, 'w') as nf:
            json.dump(user, nf, ensure_ascii=True, indent=4)


def read_pass():
    # Function to read passwords.json
    f = open(passwords_path, 'r')
    data = json.loads(f.read())
    f.close()
    return data


def clear():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
