# Javascript is Easy. Is it?

**Points** : 200

**Description**: Can you guess the password?

## Write-up
The challenge contains a login portal and the task of the challenge is to guess the correct credentials for the portal. Trying random values of username and password opens up a page saying that the credentials are wrong. 

On opening the source code, we can observe that there is a javascript function which is verying the credentials on button click. But the javascript code is not in the usual format. On researching you'll find that the javascript code has been **obfuscated**. 

Obfuscation is basically the practice of making something difficult to understand. Programs are usually obfuscated to protect intellectual property and prevent the attackers from reverse engineering.

Online JS Deobfuscator tool : http://jsnice.org/
<br>
Deobfuscated javascript code is not the usual javascript code but it is better than the obfuscated code.<br>

In the deobfuscated code, at the beginning there is an array with all the in-built functions, variable names, parameters,etc. The first two functions ord and chr are just used to get the ascii value of a characted and character from the ascii value respectively. 

In the verify function, there is if condition checking if username is equal to admin. So now we know the username is **admin**. There is a for loop in the code which can be translated to 

```
var str1 = "k5w5tds2q8`2t`45tz".split("");
var str2"8i2t`2t`u1`d1ogvt4".split("");
for(var digit=0;digit<password.length;digit++){
    password[digit] = chr(ord(password[digit]) - ord(str1[digit]) + ord(str2[digit]))
}
```
After this loop the password value is compared with the string "7h1s_1s_t0_c0nfus3"

In order to get the actual password to be entered so that we get "7h1s_1s_t0_c0nfus3" on execution of the for loop we can reverse engineer the for loop.

```
str1 = "k5w5tds2q8`2t`45tz"
str2 = "8i2t`2t`u1`d1ogvt4"
passw = "7h1s_1s_t0_c0nfus3"

password = ""
for i in range(len(passw)):
	password += chr(ord(passw[i]) + ord(str1[i])  - ord(str2[i]))
```

The correct password can be found using the above code which is indeed the flag.<br>
`flag{j4v4scr1p7_1s_34sy}`
