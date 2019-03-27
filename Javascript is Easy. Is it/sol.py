username = "admin"
str1 = "k5w5tds2q8`2t`45tz"
str2 = "8i2t`2t`u1`d1ogvt4"
password = "7h1s_1s_t0_c0nfus3"

flag = ""
for i in range(len(password)):
	flag += chr(ord(password[i]) + ord(str1[i])  - ord(str2[i]))
print(flag)
flag = ""
for i in range(len(password)):
	flag += chr(ord(str1[i]) - 1)
print(flag)
