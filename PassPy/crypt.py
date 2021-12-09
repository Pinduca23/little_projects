import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

my_data = b't1fQkMfrZzjc1VTo2XwtRhs7glVmaXK7Ne'


def encrypt(source, encode=True):
    key = SHA256.new(my_data).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(my_data).digest()
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    return data[:-padding]


"""
my_data = b't1fQkMfrZzjc1VTo2XwtRhs7glVmaXK7Ne' #this is the key
my_pass = b'this_is_the_str'


print('key: {}'.format(my_pass))
print('data: {}'.format(my_data))
encrypted = encrypt(my_pass, my_data)
print('\nenc: {}'.format(encrypted))


password = 'jhsadjsakdhjskas'
password_bytes = password.encode('ascii')
base64_bytes = base64.b64decode(password_bytes)
print(password_bytes)
print(base64_bytes)
"""
