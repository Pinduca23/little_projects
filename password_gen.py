import secrets
import string

everything = string.ascii_letters + string.digits
length = int(input("Required size of password: "))
while True:
    password = ''.join(secrets.choice(everything)for i in range(length))
    if (any(c.islower() for c in password)
            and (c.isupper() for c in password)
            and sum(c.isdigit()for c in password) >= 3):
        break

print(password)

"""
lower_case = 'abcdefghijklmnopqrstuvywz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVYWZ'
numbers = '1234567890'
symbols = '[]{}()*;/,-'

everything = lower_case + upper_case + numbers + symbols
length = 16
password = ''.join(random.sample(everything,length))
print(password)
print(check_all(password))"""
