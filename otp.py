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
print("Llave: ")
print(key_stream)
print("Mensaje cifrado: ")
print(cipher)
#print(xor_bytes(key_stream, cipher))
c = open("cifrado.txt", "wb")
c.write(cipher)
c.close()

k = open("key.txt", "wb")
k.write(key_stream)
k.close()