# Autokey Cipher

# Empty lists
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
index = 0
key = 12

# letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

plaintext = 'YOU WILL NEVER KNOW!!'

# Prepare lists for calculation
list2.append(key)
for c in plaintext:
    index+=1
    if c.isalpha():
        list1.append(L2I[c])
        list2.append(L2I[c])
    else:
        list1.append(71)
        list2.append(71)
        list4.append(c)
        list5.append(index-1)

list2.pop()
for i in range(0,(len(list1))):
    list3.append((list1[i] + list2[i]) % 26)

# encipher
ciphertext = ""
for i in range(len(list1)):
    ciphertext += I2L[list3[i]]

# decipher
plaintext2 = ""
counter = 0
for i in range(len(list1)):
    if i in list5:
        plaintext2+=list4[counter]
        counter+=1
    else:
        plaintext2 += I2L[((list3[i] - list2[i])%26)]


print ("Original Text : {}".format(plaintext))
print ("Encrypted Text : {}".format(ciphertext))
print ("Decrypted Text : {}".format(plaintext2))