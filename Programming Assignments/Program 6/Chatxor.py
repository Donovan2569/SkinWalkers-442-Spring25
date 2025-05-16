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
    return bytes([cipher[i] ^ key[i] for i in range(len(cipher))])

##### READ STDIN AS BYTES #####              
cipher_bytes = sys.stdin.buffer.read()

##### CONVERT CIPHER BYTES TO BITS #####
cipher_binary = ""
for letter in cipher_bytes:
    cipher_binary += format(letter, "08b")

##### OPEN KEY FILE AND CONVERT TO BYTES ##### 
key_file = "740cfd3199e2a52a2331528145eab143"
with open(key_file, "rb") as file_bytes:
    key_bytes = file_bytes.read()

##### CONVERT KEY BYTES TO BITS #####
key_binary = ""
for letter in key_bytes:
    key_binary += format(letter, "08b")

c_len = len(cipher_binary)
k_len = len(key_binary)
##### CHECK IF THEY ARE SAME LENGTH #####
if c_len != k_len:
    ##### IF NOT CHECK WHICH IS BIGGER #####
    ##### THEN RANDOMIZE TRAILING 1'S AND 0'S #####
    if c_len > k_len:
        key_binary += "0" * (c_len - k_len)
    else:
        cipher_binary += "0" * (k_len - c_len)
                
##### USE CRACK TO DECODE THE XOR VALUE #####      
final = (xor(cipher_bytes, key_bytes))

##### CHECK FOR REDIRECTION #####
if not sys.stdout.isatty():
    ##### WRITE BYTES TO FILE FOR REDIRECTION #####
    sys.stdout.buffer.write(final)

##### WRITE TO TERMINAL IF NOT REDIRECTION ##### 
else:
    sys.stdout.buffer.write(final)
