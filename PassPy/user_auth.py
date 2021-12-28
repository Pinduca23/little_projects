import json
from crypt import encrypt, decrypt

path = "auth_user.json"


def get_user():
    auth_username = input("Login: ").upper()
    password = input("Password: ").encode("utf-8")
    try:
        with open(path, "r", encoding="utf-8") as f:
            user_file = json.loads(f.read())
            try:
                auth_user_log = user_file.get(auth_username)
                auth_user_pass = decrypt(auth_user_log)
                if auth_user_pass == password:
                    # Returns the username and true value for the Menu.py
                    return True, auth_username
            except AttributeError:
                print("Your login/password is wrong.")
                return False, auth_username
    except FileNotFoundError:
        print("\nFile doesn't exist")


def create_user():
    username = input("Desired login: ").upper()
    password = input("Desired password: ")
    password2 = input("Repeat password: ")
    try:
        is_ok = is_unique_user(username)
        if is_ok is True:
            if password == password2:
                encrypted = encrypt(password.encode("utf-8"))
                user = {username: encrypted}
                with open(path, "r+", encoding="utf-8") as f:
                    data = json.load(f)
                    data.update(user)
                    f.seek(0)
                    json.dump(data, f, ensure_ascii=True, indent=4)
                    write_user(username)
            else:
                print("\nPasswords don't match")
        else:
            print("\nThat user already exists")
    except FileNotFoundError:
        with open(path, "w") as nf:
            encrypted = encrypt(password.encode("utf-8"))
            user = {username: encrypted}
            json.dump(user, nf, ensure_ascii=True, indent=4)
            write_user(username)


def write_user(user):
    empty_dict = {}
    user_write = {user: empty_dict}
    try:
        with open("passwords.json", "r+", encoding="utf-8") as r:
            pass_data = json.load(r)
            pass_data.update(user_write)
            r.seek(0)
            r.write(json.dumps(pass_data, indent=4, ensure_ascii=True))
    except FileNotFoundError:
        with open("passwords.json", "w") as fnf:
            json.dump(user_write, fnf, ensure_ascii=True, indent=4)


def is_unique_user(username):
    # Function to check if passwords already exists while writting
    with open(path, "r", encoding="utf-8", newline="") as f:
        data = json.load(f)
        for user in data:
            if user == username:
                return False
        else:
            return True


# create_user()
# print(is_unique_user('PINDUCA'))
# is_unique_user('PLINIO')
