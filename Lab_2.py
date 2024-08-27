#Caesar cypher

def encrypt():
    a=str(input("enter the text that has to be cyphered: "))
    b=a.lower()
    b=b.strip()
    b=b.replace(" ","")
    c=""

    for i in range(0,len(b)):
        temp=0
        temp=ord(b[i])
        temp=temp+3
        c=c+chr(temp)

    print(c)
    return c

def decrypt(c):
    d=""
    for i in range(0,len(c)):
        temp=0
        temp=ord(c[i])
        temp=temp-3
        d=d+chr(temp)
    print(d)
    return d

encrypted=encrypt()
decrypted=decrypt(encrypted)


