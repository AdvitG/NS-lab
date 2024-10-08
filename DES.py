import numpy as np
from itertools import permutations
key = np.random.randint(0,10,(4,16)) 
print(key)
perm = permutations(key) 
B=list(perm)
B=B[10]
print(B)
print("        \n")
A = np.delete(B, [7,15], 1)
print(A)

def encrypt():
    a=input("enter the text to be encrypted: ")
    a=a.strip()
    a=a.replace(" ","") 
    pass 