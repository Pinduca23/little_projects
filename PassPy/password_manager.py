import secrets
import string


pass_length = 0
while True: 
    try:
        pass_length = int(input('Required size of password: '))       
        if pass_length <= 3:
            print('Password must have at least 4 characters')
        else:
            break
    except:
        print('Not a valid number')


def alphanumeric_pass():
    while True:
        everything = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(secrets.choice(everything)for i in range(pass_length))
        if (any(c.islower() for c in password)
            and  (c.isupper() for c in password)
            and sum(c.isdigit() for c in password ) >=1):
            break
    print(password)


alphanumeric_pass()