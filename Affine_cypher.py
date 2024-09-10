def encrypt():
    a=input("enter the text to be encrypted: ")
    a=a.strip()
    a=a.replace(" ","")
    a=list(a)
    keya=3
    keyb=7
    encrypted=""
    for i in range(0,len(a)): 
        b=(keya*(ord(a[i])-97)+keyb)%26+97
        encrypted=encrypted+chr(b) 
    return  encrypted

def decrypt(a):
    a=list(a)
    keya=3
    keyb=7
    keyb=26-keyb
    print(keyb)
    c=0
    d=1
    while(c==0):
        if(keya*d%26 == 1): 
            keya=d
            c=1
         
        d=d+1
    print(keya)
    decrypted=""
    for i in range(0,len(a)): 
        b=(keya*ord(a[i])-97+keyb)%26+97
        decrypted=decrypted+chr(b) 
    return  decrypted


encryped=encrypt()
print(encryped)
print(decrypt(encryped)) 