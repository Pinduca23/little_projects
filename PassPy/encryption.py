from _typeshed import StrOrBytesPath
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt_teste():
    key = '1235467890123456'
    
    key = str.encode(key)
    key = SHA256.new(key).digest()
    print(key)

encrypt_teste()




def encrypt(key, source, encode=True):
    key1 = str.encode(key)
    encryptor = AES.new(key1, AES.MODE_CBC)
    data = encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("utf8") if encode else data

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("utf8"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding





"""def generate_key():
    # Generates a key and save in into a file
    key = Fernet.generate_key()
    with open('secret.key','wb') as key_file:
        key_file.write(key)

def load_key():
    # Loads key named `secret.key` from current directory
    return open('secret.key', 'rb').read()"""