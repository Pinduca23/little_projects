## Password Generator

This project started as a way to understand some basics about python such as:
- Functions
- Dictionaries
- DRY Principle
- Imports

The inicial code was simple, i declared all the possible strings by hand and joined them with a fixed size of 16 characters. 
```py
import random

lower_case = 'abcdefghijklmnopqrstuvywz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVYWZ'
numbers = '1234567890'
symbols = '[]{}()*;/,_-'

tudo = lower_case + upper_case + numbers + symbols
length = 16
password = ''.join(random.sample(tudo,length))
```

Then i created a function to guarantee that the passwords had at least one of each string type in it.
```py
def check_all(str):
    result_1 = False
    result_2 = False
    result_3 = False
    result_4 = False

    for i in str:
        if i in lower_case:
            result_1 = True
        if i in upper_case:
            result_2 = True
        if i in numbers:
            result_3 = True
        if i in symbols:
            result_4 = True

    return result_1 and result_2 and result_3 and result_4
```
The code was messy and not very efficient.

After the fact i discovered that you could do it more efficiently by importing 2 libraries `import string` and `import secrets` that already had the avaliable characters and with the `secrets` library you could generate strong random numbers, and with some looping you could generate a password of the desired size (at least 3 characters).
```py
import secrets
import string

everything = string.ascii_letters + string.digits
length = int(input("Required size of password: "))
password = ''.join(secrets.choice(everything)for i in range(length))
while True:
    password = ''.join(secrets.choice(everything)for i in range(length))
    if (any(c.islower() for c in password)
            and (c.isupper() for c in password)
            and sum(c.isdigit()for c in password) >= 3):
        break
```

Then with time a tried adding some "complexity" to the project, you could create XKCD(doesn't stand for anything) style passwords, then instead of just creating passwords you could read them from a JSON file and since they were already stored in a file i decided to add the option to delete saved passwords.

# The real challenge

It started when i tried adding encryption to the passwords, where i had to learn how it worked, how it's usually stored in servers (even though here i save them in JSON files and the encryption key is shown in ´crypt´ file).

In this project i'm "simulating" my database in a JSON file, i know it's not standard practice and i'm doing it just for the exercise.

After a lot of trial and error i managed to make everything work.

To run the script you're suposed to execute the `menu.py`, from there you're prompted with 2 choices. 
```
What do you wish to do?

    1 - Create a new user.
    2 - Login
    (Anything else to exit)
```
Choosing to create a new user creates a file called `auth_user.json` and `passwords.json` with auth_user beign where i store each "authorized user" and passwords where the service/passwords are stored for each user.

After creating a user you can Login and create(XKCD, alphanumeric), view or delete your passwords through this menu:
```
Please choose what you would like to do.

    1 - Generate a alphanumeric password
    2 - Generate a XKCD style password
    3 - View a password
    4 - Delete a password
    E - Exit program
```

I think i'm done with this one for now, any comments regarding best practices in my code are welcome.

And i wanted to thank @plinioh for all the help he gave during this project.

Back to my [Main Page](https://github.com/Pinduca23)
