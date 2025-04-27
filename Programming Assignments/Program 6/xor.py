import sys
from random import choice

##### CONVERT BINARY TO STRING #####
def crack(text):
    res = ""
    for i in range(0, len(text), 8):
        byte = text[i:i+8]
        res += chr(int(byte, 2))

    return res

##### XOR KEY BITS AND CIPHER BITS #####
def xor(cipher, key):
    res = ""
    for i in range(len(cipher_bytes)):
        if cipher[i] == key[i]:
            res += "0"
        else:
            res += "1"
    return res

##### READ STDIN AS BYTES #####              
cipher_bytes = sys.stdin.buffer.read()

##### CONVERT CIPHER BYTES TO BITS #####
cipher_binary = ""
for letter in cipher_bytes:
    try:
        cipher_binary += format(letter, "08b")
    except:
        pass

##### OPEN KEY FILE AND CONVERT TO BYTES ##### 
key_file = "key"
with open(key_file, "rb") as file_bytes:
    key_bytes = file_bytes.read()

##### CONVERT KEY BYTES TO BITS #####
key_binary = ""
for letter in key_bytes:
    try:
        key_binary += format(letter, "08b")
    except:
        pass

c_len = len(cipher_binary)
k_len = len(key_binary)
##### CHECK IF THEY ARE SAME LENGTH #####
if c_len != k_len:
    ##### IF NOT CHECK WHICH IS BIGGER #####
    ##### THEN RANDOMIZE TRAILING 1'S AND 0'S #####
    if c_len > k_len:
        amount = c_len - k_len
        for i in range(amount):
            key_binary += choice(["0", "1"])
    else:
        amount = k_len - c_len
        for i in range(amount):
            cipher_binary += choice(["0", "1"])
                
##### USE CRACK TO DECODE THE XOR VALUE #####      
final = crack(xor(cipher_binary, key_binary))

##### CHECK FOR REDIRECTION #####
if not sys.stdout.isatty():
    ##### WRITE BYTES TO FILE FOR REDIRECTION #####
    sys.stdout.buffer.write(bytes(final, "utf-8"))

##### WRITE TO TERMINAL IF NOT REDIRECTION ##### 
else:
    sys.stdout.write(final)
