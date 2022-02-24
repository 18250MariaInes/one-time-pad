"""import onetimepad

msg = open("cifrado.txt", "r")
text = msg.read()
msg.close()
print("MENSAJE A DESCIFRAR: ")
print(text)

key = open("key.txt", "r")
llave = key.read()
key.close()
print("LLAVE ")
print(llave)

msg = onetimepad.decrypt(text, llave)
print("Mensaje descifrado es: ")
print(msg)"""

import random

def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i]^ message[i] for i in range(length)])

# this is done by your enemy
msg = open("cifrado.txt", "r")
message = msg.read()
message =  bytes(message, 'utf-8')
msg.close()
#print(message)

k = open("key.txt", "r")
key = k.read()
key = bytes(key, 'utf-8')
#print(key)
k.close()

print(xor_bytes(key, message))