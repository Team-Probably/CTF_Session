## Imposters

### Description

I hid flag in this file but now even I can't open it :(

[hint.pdf](./hint.pdf)


**Points**: 300

----------------------------------------------------

##### Hints to the Solution

> Are you sure its a PDF?
> Look up LSB Encoding

##### Steps to the Solution
* When you do a hexdump of the file, you see something odd is up with the magic numbers. It ain't a PDF. It's a GIF!
* Just changing the extension to .gif allows us to open the file!
* LSB?? As in LSB Encoding???


```py
binary_data = open("hint.gif","rb") # Open the file binary mode
# binary_data.seek(80)  #seek to 54 bytes these bytes does not contain any data
data = binary_data.read() # read the binary data
# print(data)
l = [] 
for i in data:
    l.append(bin(i)[-1])  #make a list of LSB bits
for i in range(0,5000,8):
    print(chr(int(''.join(l[i:i+8]),2)),end='') # print the character
```