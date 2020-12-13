import encrypt
import generateKey

#Decrypt message
decryptedM = []
for element in encrypt.c:
    decryptedM.append((element ** generateKey.d) % generateKey.n)

#Reverse the padding scheme
finalMessage = ""
for element in decryptedM:
    finalMessage = finalMessage + str(chr(element))

print(finalMessage)
