# AES Baby

**Points** : 50

**Description**: AES is one of the basic block ciphers but has some awesome exploits(Not this one though)

## Write-up
A zip file has been provided which contains the ciphertext and the encryption script encrypt.py that was used. 

This is a very simple AES encryption challenge wherein the key has been provided along with the mode that was used `AES-ECB`.

All we need to do is use this key to decrypt the ciphertext using the following code
```
from Crypto.Cipher import AES
from Crypto.Util.number import *
def pad(s):
    s += chr(16 - len(s)%16)*(16 - len(s)%16)
    return s

key = bytes('dont_use_aes_ecb','utf-8')
ciphertext = open("ciphertext.txt").read()
ciphertext = bytes.fromhex(cifrom Crypto.Cipher import AES
from Crypto.Util.number import *
def pad(s):
    s += chr(16 - len(s)%16)*(16 - len(s)%16)
    return s

key = bytes('dont_use_aes_ecb','utf-8')
flag = open("flag.txt").read()
obj1 = AES.new(key, AES.MODE_ECB)
ct = obj1.encrypt(pad(flag))
open("ciphertext.txt",'w').write(ct.hex())phertext)
obj1 = AES.new(key, AES.MODE_ECB)
flag = obj1.decrypt(ciphertext)
```