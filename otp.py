"""import onetimepad
import random

def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i]^ message[i] for i in range(length)])

msg = open("mensaje.txt", "r")
text = msg.read()
text = text.encode
msg.close()
print("MENSAJE A CIFRAR: ")
print(text)

key_stream = generate_key_stream(len(text))
cipher = xor_bytes(key_stream, text)

c = open("cifrado.txt", "w")
c.write(cipher)
c.close()

k = open("key.txt", "w")
k.write(key_stream)
k.close()
print("MENSAJE SECRETO GUARDADO")"""
"""print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'SHOMTDECQTILCHZSSIXGHYIKDFNNMACEWRZLGHRAQQVHZGUERPLBBQC')

print(msg)"""

import random

def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i]^ message[i] for i in range(length)])

msg = open("mensaje.txt", "r")
message = msg.read()
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)
print(key_stream)
print(cipher)
#print(xor_bytes(key_stream, cipher))
c = open("cifrado.txt", "w")
c.write(str(cipher))
c.close()

k = open("key.txt", "w")
k.write(str(key_stream))
k.close()