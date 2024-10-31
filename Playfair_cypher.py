import numpy as np

def encrypt():
    a=input("enter the text to be encrypted: ")
    c=a.strip()
    c=c.replace(" ","")
    c=c.replace("j","i")
    key=makekeymatrix("money")
    print(key)
    c=list(c) 
    looplength=len(c)-1
    for i in range(0,looplength ): 
        if c[i]==c[i+1]: 
            c.insert(i+1,"x")
            looplength=looplength+1
    lenc=len(c)
    if lenc%2==1: 
        c.append("z")
    print(c)
    encrypted=""
    
    for i in range(0,len(c),2):
        temp=np.where(key == c[i])
        temp1=np.where(key == c[i+1])
        if temp[0]==temp1[0]:
            encrypted=encrypted+key[temp[0][0]][temp[1][0]+np.int64(1)]
            encrypted=encrypted+key[temp1[0][0]][temp1[1][0]+np.int64(1)]
        if temp[1]==temp1[1]: 
            encrypted=encrypted+key[temp[0][0]+np.int64(1)][temp[1][0]]
            encrypted=encrypted+key[temp1[0][0]+np.int64(1)][temp1[1][0]]
        else: 
            pass
    

        
    print(encrypted)

def makekeymatrix(key): 
    for i in range(0,len(key)): 
        #print(i)
        pass
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

def decrypt(c):
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

a=encrypt()
#b=decrypt(a)


