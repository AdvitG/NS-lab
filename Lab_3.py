
import numpy as np

def encrypt():
    
    a=input("enter the phrase to be encrypted:" )
    a=a.lower()
    a=a.strip()
    a=a.replace(" ","")
    #preparing the input for encryption


    b=len(a)%2 #since we are encrypting using 2d keys we are going to device input into 2 charecters. checking to see even charecters to add placeholder if needed

    key=[[1, 2],[3, 4]]
    key=np.array(key)
    
    encrypted=""
    if b==1:
        a=a+"a"
    for i in range(0,len(a),2):
        c=np.array([[ord(a[i])-97],[ord(a[i+1])-97]])
        encryptt=key@c
        encryptt=encryptt%26
        encrypted=encrypted+chr(encryptt[0,0]+97)
        encrypted=encrypted+chr(encryptt[1,0]+97)
    
    print(encrypted)


def decrypt(): 
    print("pass")
    
encrypt()

