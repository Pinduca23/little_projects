from base64 import decode
import secrets
import string
import json
import os
import pyperclip as pc
from crypt import encrypt, decrypt


def pass_size():
    # Gets desired password length
    while True:
        pass_length = 0
        while pass_length < 4:
            try:
                pass_length = int(input('\nRequired size of password: '))
                if pass_length <= 3:
                    print('\nPassword must have at least 4 characters or words')
                else:
                    return pass_length
            except ValueError:
                print('\nNot a valid number')


# Declaring user dict
user = {}


def xkcd_password():
    # Creating XKCD passwords made up of word list from .txt
    length = pass_size()
    with open(file='PassPy\words.txt') as o:
        words = [word.strip() for word in o]
        password = ' '.join(secrets.choice(words)
                            for i in range(length)).title()
    clear()
    encrypt_write(password)


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
    clear()
    encrypt_write(password)


def get_password():
    # Function to get passwords
    data_from = input('Which password would you like to see? \n').upper()
    data = read_pass()
    password = data.get(data_from)
    if password == None:
        print('\nPassword for that login doesn''t exist')
    else:
        clear()
        decrypted = decrypt(password)
        decrypted = decrypted.decode('ascii')
        print('\nThe password for', data_from.title(),
              'is:', decrypted)
        print('\nPassword copied to clipboard!')
        pc.copy(decrypted)


def delete_pass():
    # Function to delete password from matching login
    data_from = input(
        '\nWich login/password would you like to delete?: ').upper()
    data = read_pass()
    login = data.get(data_from)
    if login == None:
        print('\nThat login doesn''t exist')
    else:
        accept = input(f'Are you sure you wish to delete the password from:{data_from} Y/n').upper()
        if accept == 'Y':
            del data[data_from]
            with open(passwords_path, 'w') as file_data:
                json.dump(data, file_data)
        else:
            ()


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


def encrypt_write(password):
    user_log = input('\nWhat is this password for?: ').upper()
    print('\nYour new password:\n', password)
    password_bytes = password.encode('ascii')
    encrypted = encrypt(password_bytes)
    user = {user_log: encrypted}
    write_pass(user)

alphanumeric_pass()
get_password()
