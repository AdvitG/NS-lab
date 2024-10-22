p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)
k = 2
d = (1 + (k*phi))/e
def encrypt(msg):
    c = pow(msg, e)
    c = c%n
    print("Encrypted = ", c)
    return c
def decrypt(c): 
    m = pow(c, d)
    m = m%n
    print("decrypted = ", m)
c=encrypt(10)
decrypt(c)