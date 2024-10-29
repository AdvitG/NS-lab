import math
p = 53
q = 59
n = p*q #public key generated
phi = (p-1)*(q-1) #calculating phi
#for e: 1<e< phi(n) ; gcd(phi(n),e)=1
#lets take initial value of e =2
e=2 

while True: 
    if math.gcd(e,phi)==1: 
        break
    else: 
        e=e+1

#e selected

k = 2 
d=1
while True: 
    if (e*d)%phi==1: 
        break
    else: 
        d=d+1
#choosing D

def encrypt(msg):
    c = (msg**e)
    c = c%n
    print("Encrypted = ", c)
    return c
def decrypt(c): 
    m = c**d
    m = m%n
    print("decrypted = ", m)



c=encrypt(89)
decrypt(c)