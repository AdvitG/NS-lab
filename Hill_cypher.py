import numpy as np
def encrypt():
    a=input("enter the phrase to be encrypted:" )
    a=a.lower()
    a=a.strip()
    a=a.replace(" ","")
    #preparing the input for encryption
    b=len(a)%2 #since we are encrypting using 2d keys we are going to device input into 2 charecters. checking to see even charecters to add placeholder if needed
    key=[[3, 3],[2, 5]]
    key=np.array(key)
    encrypted=""
    if b==1:
        a=a+"a"
    for i in range(0,len(a),2):
        c=np.array([[ord(a[i])-97],[ord(a[i+1])-97]])
        encryptt=(key@c)%26
        encrypted=encrypted+chr(encryptt[0,0]+97)
        encrypted=encrypted+chr(encryptt[1,0]+97)
    return encrypted
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  
    det_inv = mod_inverse(det, modulus)  
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod {}".format(modulus))
    adjugate_matrix = np.array([[matrix[1, 1], -matrix[0, 1]], 
                                [-matrix[1, 0], matrix[0, 0]]])
    
    inv_matrix = (det_inv * adjugate_matrix) % modulus
    return inv_matrix
def decrypt(a): 
    key=[[3, 3],[2, 5]]
    key=np.array(key)
    inv_key = matrix_mod_inverse(key, 26)
    decrypted=""
    for i in range(0,len(a),2):
        c = np.array([[ord(a[i]) - 97], [ord(a[i + 1]) - 97]])
        decryptt = (inv_key @ c) % 26
        decrypted += chr(int(decryptt[0, 0]) + 97)
        decrypted += chr(int(decryptt[1, 0]) + 97)
    return decrypted
a=encrypt()
print(a) 
b=decrypt(a)
print(b)
