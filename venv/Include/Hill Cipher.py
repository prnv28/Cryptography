import numpy
from numpy import matrix
from numpy.linalg import inv

key = matrix('6 24 1; 13 16 10; 20 17 15')
plaintext = matrix('2 14 3; 8 18 17; 0 3 24')
ciphertext=(plaintext*key)%26
print("Plain Text : \n{}".format(plaintext))
print("Key : \n{}".format(key))
print("Cipher Text : \n{}".format(ciphertext))

# Find Multiplicative Inverse of given key
def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

determinant = numpy.linalg.det(key).astype(int)
print("Determinant : \n{}".format(determinant))

mulinvdeterminant = modInverse(determinant,26)
print("Multiplicative Inverse : \n{}".format(mulinvdeterminant))

power = ((inv(key)*determinant))%26
power2 = (mulinvdeterminant*power)%26
power3 = numpy.round(power2)
power4 = power3.astype(int)
print("Requried matrix is : \n{}".format(power4))

Decryptedtext = (ciphertext*power4)%26
print("Decrypted Text : \n{}".format(Decryptedtext))

