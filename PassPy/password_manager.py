import secrets
import string
import json
import pyperclip as pc
from crypt import encrypt, decrypt


def pass_size():
    # Gets desired password length
    while True:
        pass_length = 0
        while pass_length < 4:
            try:
                pass_length = int(input("\nRequired size of password: "))
                if pass_length <= 3:
                    print(
                        "\nPassword must have at least 4 characters or words"
                    )
                else:
                    return pass_length
            except ValueError:
                print("\nNot a valid number")


def xkcd_password(auth_user):
    # Creating XKCD passwords made up of word list from .txt
    length = pass_size()
    with open(file="PassPy/words.txt") as o:
        words = [word.strip() for word in o]
        password = " ".join(
            secrets.choice(words) for i in range(length)
        ).title()
    encrypt_write(password, auth_user)


def alphanumeric_pass(auth_user):
    # Creating passwords from numbers/letters/symbols
    length = pass_size()
    while True:
        everything = string.ascii_letters + string.punctuation + string.digits
        password = "".join(secrets.choice(everything) for i in range(length))
        if (
            any(c.islower() for c in password)
            and (c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            break
    encrypt_write(password, auth_user)


def get_password(auth_user):
    # Function to get passwords
    data_from = input("Which password would you like to see? \n").upper()
    f = open(passwords_path, "r")
    data = json.loads(f.read())
    user_data = data.get(auth_user)
    while True:
        for i in user_data:
            if data_from == i:
                password = data[auth_user][data_from]
                decrypted = decrypt(password)
                decrypted = decrypted.decode("utf-8")
                print(
                    "\nThe password for", data_from.title(), "is:", decrypted
                )
                print("\nPassword copied to clipboard!")
                pc.copy(decrypted)
        break
    print(f"There's no password for {data_from.title()} service")


def delete_pass(auth_user):
    # Function to delete password from matching login
    data_from = input(
        "\nWich login/password would you like to delete?: "
    ).upper()
    # unique_pass(auth_user, data_from)
    f = open(passwords_path, "r")
    data = json.load(f)
    user_data = data.get(auth_user)
    while True:
        for i in user_data:
            if data_from == i:
                accept = input(
                    f"Are you sure you wish to delete the password from:{data_from.title()} Y/n: "
                ).upper()
                if accept == "Y":
                    del user_data[data_from]
                    with open(passwords_path, "w") as file_data:
                        json.dump(data, file_data, ensure_ascii=True, indent=4)
                elif accept == "N":
                    delete_pass(auth_user)
                else:
                    print("\nNot a valid option")
                break



# JSON file path where passwords area stored.
passwords_path = "PassPy/passwords.json"


def encrypt_write(password, auth_user):
    # Function to write encrypted passwords to JSON
    while True:
        data_from = input("\nWhat is this password for?: ").upper()
        try:
            is_ok = unique_pass(auth_user, data_from)
            if is_ok is True:
                print(f"The password for {data_from.title()} already exists")
                break
        except FileNotFoundError:
            pass
        print(f"\nYour new password: {password}\n")
        encrypted = encrypt(password.encode("utf-8"))
        user = {data_from: encrypted}
        user_pass = {auth_user: user}
        try:
            with open(passwords_path, "r+", encoding="utf-8", newline="") as f:
                pass_data = json.load(f)
                for user_in_file in pass_data:
                    if user_in_file == auth_user:
                        pass_data[auth_user][data_from] = encrypted
                f.seek(0)
                f.write(json.dumps(pass_data, ensure_ascii=True, indent=4))
                break
        except FileNotFoundError:
            with open(passwords_path, "w") as nf:
                json.dump(user_pass, nf, ensure_ascii=True, indent=4)
            break


def unique_pass(auth_user, data_from):
    # Function to check if passwords already exists while writting
    with open(passwords_path, "r", encoding="utf-8", newline="") as f:
        data = json.load(f)
        user_data = data.get(auth_user.upper())
        while True:
            for i in user_data:
                if i == data_from:
                    is_ok = True
                    break
                else:
                    is_ok = False
            return is_ok


# auth_user = "ramon"
# delete_pass(auth_user)
# alphanumeric_pass(auth_user)
# get_password(auth_user)
# print(unique_pass(auth_user, 'REDDIT'))