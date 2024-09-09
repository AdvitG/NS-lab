import numpy as np

def encrypt():
    a=input("enter the text to be encrypted: ")
    c=a.strip()
    c=c.replace(" ","")
    key=makekeymatrix("money")
    print(key)
    lenc=len(c)
    if lenc%2==1: 
        c=c+"z"
    c=list(c) 
    for i in range(0, len(c)): 
        if c[i]==c[i+1]: 
            c.insert(i+1,"x")
    print(c)


    


def makekeymatrix(key): 
    for i in range(0,len(key)): 
        print(i) 
    arrkey=key
    b=[]
    for k in range(0,len(key)): 
        b.append(ord(key[k]))
    for j in range(0+97,26+97): 

        if j==106 or j in b: 
            pass 
        else: arrkey=arrkey+ chr(j)

    listkey=list(arrkey)

    linear_array=np.array(listkey)
    reshaped_array = linear_array.reshape(5, 5)

    return reshaped_array







encrypt()


