import secrets
import string

def alphanumeric_pass():
    pass_length = 0
    while True:
        try:
            
            if pass_length < 4:
                pass_length = int(input('Required size of password: '))
                print('Password must have at least 4 characters')
            else:
                break
        except:
            print('Not a valid number')
        everything = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(secrets.choice(everything)for i in range(pass_length))
        if (any(c.islower() for c in password)
            and  (c.isupper() for c in password)
            and sum(c.isdigit() for c in password ) >=4):
            break
    print(password)


alphanumeric_pass()