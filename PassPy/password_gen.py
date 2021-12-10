from os import write
import secrets
import string
import json




users = {'teste_chave': 'teste_valor'}
print(users)

def words_pass():
    with open('D:\PyProjectLuis\little_projects\wpa2-wordlists\PlainText\words.txt') as f:
        words = [(word.strip().capitalize()) for word in f]
        length = 0
        account_name = input('Where is this password for?: ').upper()
        while True:
            try:
                if length < 1:
                    length = int(input("Required size of password: "))
                else:
                    break
            except ValueError:
                print('Not a valid number')
        password = ''.join(secrets.choice(words) for i in range(length))
    print(password)
    #encrypt(account_name, password)
    users = {account_name: password}
    #print(users)
    write_password(users)

    # First things first, learn to save to file and read that file
    # later we can try and figure out how to encrypt data.


def alphanumeric():
    everything = string.ascii_letters + string.digits + string.punctuation
    length = 0
    account_name = input('Where is this password for?: ').upper()
    while True:
        try:
            if length < 3:
                length = int(input("Required size of password: "))
            else:
                break
        except ValueError:
            print('Not a valid number')
        password = ''.join(secrets.choice(everything)for i in range(length))
        if (any(c.islower() for c in password)
                and (c.isupper() for c in password)
                and sum(c.isdigit()for c in password) >= 3):
            break
    print(password)
    users = {account_name: password}
    write_password(users)
    # Agora tem que salvar em um arquivo pra depois encriptar 


def insert_password():
    account_name = input('What is this password for?: ').upper
    password = str(input('Please insert your password: '))
    users = {account_name: password}
    write_password(users)




def search_password():
    account_name = input("What account do you wish to view?: ")
    print('Looking for password')


def view_passwords():
    print('Viewing all passwords')


def write_password(users):
    file_path = 'D:\PyProjectLuis\little_projects\PassPy\passwords.json'
    with open(file_path, 'a', encoding='utf-8') as p:
        json.dump(users, p, ensure_ascii=False, indent=4)


words_pass()

#alphanumeric()