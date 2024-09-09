import numpy as np

def encrypt():
    a=input("enter the text to be encrypted: ")
    c=a.strip()
    c=c.replace(" ","")
    c=c.replace("j","i")
    key=makekeymatrix("money")
    print(key)
    c=list(c) 
    for i in range(0, len(c)): 
        if c[i]==c[i+1]: 
            c.insert(i+1,"x")
    lenc=len(c)
    if lenc%2==1: 
        c=c+"z"
    print(c)
    encrypted=""
    for i in range(0,len(c),2):
        #temp=np.array([(c[i]),(c[i+1])])
        temp=list(zip(*np.where(key == c[i])))
        temp1=list(zip(*np.where(key == c[i+1])))

        #creating condition list

        if temp[0][1]==temp1[0][1]: 
            pass 

            #encrypted=encrypted+key[]
        if temp[0][0]==temp1[0][0]: 
            print(temp)
        else: 
            pass



        print(temp)
        print(temp1)

    


    


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


