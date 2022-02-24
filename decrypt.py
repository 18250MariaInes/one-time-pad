import random

def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i]^ message[i] for i in range(length)])

# this is done by your enemy
msg = open("cifrado.txt", "rb")
message = msg.read()
#message =  bytes(message, 'utf-8')
print("Mensaje cifrado: ")
print(message)
print("*"*50)
msg.close()
#print(message)

print("Llave: ")
k = open("key.txt", "rb")
key = k.read()
#key = bytes(key, 'utf-8')
print(key)
print("*"*50)
#print(key)
k.close()

print(xor_bytes(key, message))