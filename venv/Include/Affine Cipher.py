# Affine Cipher

# letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key = 3
key1 = int(input("Enter K : "))

# Find Multiplicative Inverse of given key
def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

key2 = modInverse(key1,26)

# Check key is valid?
if key2 == 1:
    print("Please Enter Valid Key.")
    exit()


plaintext = "YOU WILL NEVER KNOW!!!"

# encipher
ciphertext = ""
for c in plaintext.upper():
    if c == ' ' or c == '\n' or c == '!':
        ciphertext = ciphertext + c
    else:
        ciphertext = ciphertext + I2L[ (L2I[chr((((ord(c) - 65) * key1) % 26) + 65)] + key)%26 ]

# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c == ' ' or c == '\n' or c == '!':
        plaintext2 = plaintext2 + c
    else:
        plaintext2 = plaintext2 + I2L[ (L2I[chr((((ord(c) - 65) * key2) % 26) + 65)] - key)%26 ]

print ("Original Text : {}".format(plaintext))
print ("Encrypted Text : {}".format(ciphertext))
print ("Decrypted Text : {}".format(plaintext2))

