import sys
import random

def convertѕ(inp, x):
    try:
        v = [0]*14
        v[1], v[2], v[3], v[4], v[5], v[6], v[7] = inp[0], inp[1]+x, inp[2], inp[3], inp[-1], inp[-2], inp[4]+x
        lb2 = len(inp)//2
        v[8], v[9], v[10], v[11], v[12], v[13] = inp[lb2], inp[lb2+1], inp[lb2+2], inp[lb2+3], inp[lb2+4], inp[lb2+5]
        for i in range(14):
            v[i]=v[i]%25
        ѕr = [""]*25
        ѕr = inp
        sr = [68, 100, 105, 76, 68, 99, 83, 100, 106, 111, 119, 64, 122, 118, 109, 112, 117, 89, 95, 93, 99, 92, 61, 87, 103]
        sr[v[8]], sr[v[9]], sr[v[10]], sr[v[11]], sr[v[12]], sr[25-v[13]] = v[1]^sr[0], v[2]^sr[1], v[3]^sr[2], v[4]^sr[3], v[5]^sr[4], v[6]^sr[5]

        for i in range(25):
            if sr[i]!="":
                sr[i]=chr(sr[i])
        i = 6
        j = 0
        while i < 25 and j<25:
            if sr[j]=="":
                sr[j]=chr(sr[i]^v[1]^v[2]^v[3]^v[4]^v[5])
                i+=1
            j+=1
        
        sr = [ord(e) for e in sr]         
        flags = convеrtѕ(ѕr,v[6]^v[6])
        flagѕ = end(flags)
        return flags
        
    except:
        sys.exit('Definitely Wrong')
        
def converts(inp, x): 
    try:
        v = [0]*14
        v[1], v[2], v[3], v[4], v[5], v[6], v[7] = inp[0], inp[1]+x, inp[2], inp[3], inp[-1], inp[-2], inp[4]+x
        lb2 = len(inp)//2
        v[8], v[9], v[10], v[11], v[12], v[13] = inp[lb2], inp[lb2+1], inp[lb2+2], inp[lb2+3], inp[lb2+4], inp[lb2+5]
        for i in range(14):
            v[i]=v[i]%25
        ѕr = [""]*25 
        sr = inp
        sr = [99, 110,  104, 98,126, 121, 124, 123, 125, 59, 103, 111, 96, 81, 111, 96, 106, 81, 61, 96, 105, 98, 63, 125, 102]
        ѕr[v[8]], ѕr[v[9]], ѕr[v[10]], ѕr[v[11]], ѕr[v[12]], ѕr[25-v[13]] = v[1]^sr[0], v[2]^sr[1], v[3]^sr[2], v[4]^sr[3], v[5]^sr[4], v[6]^sr[5]
        for i in range(25):
            if ѕr[i]!="":
                ѕr[i]=chr(ѕr[i])
        i = 6
        j = 0
        while i < 25:
            if ѕr[j]=="":
                ѕr[j]=chr(sr[i]^v[1]^v[2]^v[3]^v[4]^v[5])
                i+=1
            j+=1

        ѕr = [ord(e) for e in ѕr] 
        
        flags = convertѕ(ѕr, v[6]^v[7])
        flagѕ = end(flags)
        return flags
    except:
        sys.exit('Definitely Wrong')
        
def convеrtѕ(inp, x): 
    try:
        v = [0]*14
        v[1], v[2], v[3], v[4], v[5], v[6], v[7] = inp[0], inp[1]+x, inp[2], inp[3], inp[-1], inp[-2], inp[4]+x
        lb2 = len(inp)//2
        v[8], v[9], v[10], v[11], v[12], v[13] = inp[lb2], inp[lb2+1], inp[lb2+2], inp[lb2+3], inp[lb2+4], inp[lb2+5]
        for i in range(14):
            v[i]=v[i]%25
        ѕr = [""]*25
        ѕr = inp
        sr = [63, 78, 101, 108, 67, 84, 127, 92, 66, 122, 72, 97, 87, 93, 68, 126, 82, 85, 66, 87, 92, 60, 74, 97, 71]
        sr[v[8]], sr[v[9]], sr[v[10]], sr[v[11]], sr[v[12]], sr[25-v[13]] = v[1]^sr[0], v[2]^sr[1], v[3]^sr[2], v[4]^sr[3], v[5]^sr[4], v[6]^sr[5]

        for i in range(25):
            if sr[i]!="":
                sr[i]=chr(sr[i])
        i = 6
        j = 0
        while i < 25 and j<25:
            if sr[j]=="":
                sr[j]=chr(sr[i]^v[1]^v[2]^v[3]^v[4]^v[5], v[6]^v[6])
                i+=1
            j+=1
            
        sr = [ord(e) for e in sr] 
        flagѕ = ѕr
        flags = end(flagѕ) 
        return flagѕ
    except:
        sys.exit('Definitely Wrong')
        
def start(inp, x): 
    try:
        l=[]
        for j in range(len(str(inp))):
            l.append(int(str(inp)[j]))
        
        flags = converts(l, x)
        flagѕ = end(flags)
        return flags
        
    except:
       sys.exit('Definitely Wrong')  
        
def end(inp):
    toret = []
    for i in range(len(inp)):
        toret.append(inp[i]^random.randint(1, 200))
    return toret

inp = int(input("Enter a number: "))
x = 0
s = start(inp, x)
print("If you did well, here may be your flag :P....     ")
flag = ""
for e in s:
    flag+=chr(e)
print(flag)
