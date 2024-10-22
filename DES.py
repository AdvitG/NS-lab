import numpy as np
from itertools import permutations
def generatekey(): 
    key = np.random.randint(0,2,(4,16)) 
    perm = permutations(key) 
    B=list(perm)
    B=B[10]
    A = np.delete(B, [7,15], 1)
    B=np.split(A, 2, axis=1)
    print(B)
    return B


def convert_input_to_matrix(a):
    pass 

def take_input():
    a=input("enter the text that you want to encrypt: ")
    if len(a)%8 != 0: 
        b=len(a)%8
        a=a+"-"*(8-b)
    return a

def encrypt():
    LK=key[0]
    RK=key[1]
    print(LK)
    plaintext=take_input()
    for i in range(0,len(plaintext),8): 
        a=plaintext[i:i+8]
        block=[]
        for j in range(0,8): 
            b=bin(ord(a[j]))[2:].zfill(8)
            b=list(b)
            block=block+b
        block=np.array(block)
        block=np.reshape(block, (8, 8))
        C=np.split(block, 2, axis=1)
        BL=C[0]
        BR=C[1]
        
    
    



    
key=generatekey()  
encrypt()
    