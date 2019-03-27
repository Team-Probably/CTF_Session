from Crypto.Cipher import AES
from Crypto.Util.number import *
def pad(s):
    s += chr(16 - len(s)%16)*(16 - len(s)%16)
    return s

key = bytes('dont_use_aes_ecb','utf-8')
flag = open("flag.txt").read()
obj1 = AES.new(key, AES.MODE_ECB)
ct = obj1.encrypt(pad(flag))
open("ciphertext.txt",'w').write(ct.hex())