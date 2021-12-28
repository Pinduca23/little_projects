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
    with open(file="words.txt") as o:
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
    data_from = input("\nWhich password would you like to see? ").upper()
    f = open(passwords_path, "r")
    data = json.loads(f.read())
    user_data = data.get(auth_user)
    while True:
        for passwords in user_data:
            if data_from == passwords:
                password = data[auth_user][data_from]
                decrypted = decrypt(password)
                decrypted = decrypted.decode("utf-8")
                print(
                    "\nThe password for", data_from.title(), "is:", decrypted
                )
                print("\nPassword copied to clipboard!")
                pc.copy(decrypted)
                return False
        else:
            print(f"\nThere's no password for {data_from.title()} service")
            return False


def delete_pass(auth_user):
    # Function to delete password from matching login
    data_from = input(
        "\nWich login/password would you like to delete?: "
    ).upper()
    # is_unique_pass(auth_user, data_from)
    f = open(passwords_path, "r")
    data = json.load(f)
    user_data = data.get(auth_user)
    while True:
        for passwords in user_data:
            if data_from == passwords:
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
        else:
            print("\n That login/passwords does not exist")
            return False


# JSON file path where passwords area stored.
passwords_path = "passwords.json"


def encrypt_write(password, auth_user):
    # Function to write encrypted passwords to JSON
    while True:
        data_from = input("\nWhat is this password for?: ").upper()
        try:
            is_ok = is_unique_pass(auth_user, data_from)
            if is_ok is False:
                print(f"\nThe password for {data_from.title()} already exists")
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


def is_unique_pass(auth_user, input_password):
    # Function to check if passwords already exists while writting
    with open(passwords_path, "r", encoding="utf-8", newline="") as f:
        data = json.load(f)
        user_passwords = data.get(auth_user)
        for password in user_passwords:
            if password == input_password:
                return False
        else:
            return True


# auth_user = "plinio"
# delete_pass(auth_user)
# alphanumeric_pass(auth_user)
# et_password(auth_user)
# print(is_unique_pass('SOUZA', 'MU ONLINE'))
