# My simple projects
Simple python projects designed for learning some basic functions

###### Password.py
Is a program made with the intent of learning about imports, join and string splitting

It may have started that way, pretty simple as show in the code snippet bellow
```
lower_case = 'abcdefghijklmnopqrstuvywz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVYWZ'
numbers = '1234567890'
symbols = '[]{}()*;/,-'

everything = lower_case + upper_case + numbers + symbols
length = 16
password = ''.join(random.sample(everything,length))
print(password)
print(check_all(password))
```

But i found out that there's a library with all characters declared already so i dont have to manually insert them.
`import string`
And instead of using `random` i found the `secrets` module that was made with the sole purpose of generating strong random numbers for data such as passwords.


