import json
from crypt import encrypt, decrypt

path = 'PassPy/auth_user.json'


def get_user():
    auth_username = input('Login: ')
    password = input('Password: ').encode('utf-8')
    try:
        f = open('PassPy/auth_user.json', 'r')
        user_file = json.loads(f.read())
        f.close()
        try:
            auth_user_log = user_file.get(auth_username)
            auth_user_pass = decrypt(auth_user_log)
            if auth_user_pass == password:
                return True, auth_username
        except AttributeError:
            #print('Your login/password is wrong.')
            return False, auth_username
    except FileNotFoundError:
        print('File doesn''t exist')


def create_user():
    username = input('Desired login: ')
    password = input('Desired password')
    password2 = input('Desired password')
    if password == password2:
        password.encode('utf-8')
        encrypted = encrypt(password)
        user = {username: encrypted}
        try:
            with open(path, 'r+', encoding='utf-8') as f:
                data = json.load(f)
                data.update(user)
                f.seek(0)
                json.dump(data, f, ensure_ascii=True, indent=4)
            f.close()
        except FileNotFoundError:
            with open(path, 'w') as nf:
                json.dump(user, nf, ensure_ascii=True, indent=4)
