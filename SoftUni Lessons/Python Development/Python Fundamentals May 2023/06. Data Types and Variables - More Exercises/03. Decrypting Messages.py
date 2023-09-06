# On the first line, you will receive a key (integer)
key = int(input())

# On the second line, you will receive n – the number of lines, which will follow.
n = int(input())

# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.

message = ''

for line in range(n):
    message += chr(ord(input()) + key)

# In the end, print the decrypted message
print(message)
