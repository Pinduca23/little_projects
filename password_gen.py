import random

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



lower_case = 'abcdefghijklmnopqrstuvywz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVYWZ'
numbers = '1234567890'
symbols = '[]{}()*;/,-'

everything = lower_case + upper_case + numbers + symbols
length = 16
password = ''.join(random.sample(everything,length))
print(password)
print(check_all(password))