import generateKey

message = input("What is your message?\n")
#Padding scheme using Ascii
M = []
for i in range(0, len(message)):
    M.append(ord(message[i]))



#encrypt message:
c = []
for l in M:
    c.append((l ** generateKey.e) % generateKey.n)


