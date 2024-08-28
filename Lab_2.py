#Caesar cypher
def encrypt():
    a=input("enter the text that has to be cyphered: ")
    b=a.lower()
    b=b.strip()
    b=b.replace(" ","")
    c=""
    for i in range(0,len(b)+1):
        temp=ord(b[i-1])
        temp=temp+3
        c=c+chr(temp) 

    return c

def decrypt(b): 
    c=""
    for i in range(0,len(b)+1):
        temp=ord(b[i-1])
        temp=temp-3
        
        c=c+chr(temp) 
    return c

a=encrypt()
print(decrypt(a))