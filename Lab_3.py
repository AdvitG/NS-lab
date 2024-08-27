
import numpy as np

def encrypt():
    
    a=input("enter the phrase to be encrypted:" )
    a=a.lower()
    a=a.strip()
    a=a.replace(" ","")
    b=len(a)%2
    key=[[1,2][3,4]]
    key=np.array(key)
    if b==1:
        a=a+"a"
    for i in range(0,len(a),2):
        c=numpy.array([ord(a[i])-97,ord(a[i+1])-97])
        print(c)



    if b==1:
        a=a[0:len(a)-1]
    
encrypt()

