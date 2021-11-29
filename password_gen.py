import random

lower_case = 'abcdefghijklmnopqrstuvywz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVYWZ'
numbers = '1234567890'
symbols = '[]{}()*;/,_-'

tudo = lower_case + upper_case + numbers + symbols
length = 16
password = ''.join(random.sample(tudo,length))
print(password)