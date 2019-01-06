# Monoalphabetic mapping cipher

import random

# key and value lists
list1 = []
list2 = ['B', 'Q', 'W', 'T', 'N', 'O', 'R', 'J', 'D', 'H', 'Y', 'E', 'F', 'P', 'U', 'M', 'V', 'I', 'L', 'A', 'Z', 'X',
         'C', 'S', 'K', 'G']
# Shuffle values
random.shuffle(list2)

for i in range(65,91):
    list1.append(chr(i))

dictionary = dict(zip(list1,list2))

plaintext = "YOU WILL NEVER KNOW!!!"

# encipher
ciphertext = ""
for c in plaintext:
    if c in dictionary.keys():
        ciphertext += dictionary[c]
    else:
        ciphertext += c

# Dictionary {key - value} to {value - key} Inversion
invertdictionary = dict([[value, key] for key, value in dictionary.items()])

# decipher
plaintext2 = ""
for c in ciphertext:
    if c in invertdictionary.keys():
        plaintext2 += invertdictionary[c]
    else:
        plaintext2 += c

print ("Original Text : {}".format(plaintext))
print ("Encrypted Text : {}".format(ciphertext))
print ("Encrypted Text : {}".format(plaintext2))
