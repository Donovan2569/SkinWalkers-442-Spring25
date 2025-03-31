# Program 2: Vigenere
# CSC 442: Intro to Cybersecurity - Group 4
# 3/31/25

import sys

def encrypt(text, Key):
    count = 0  #tracks current position in Key; wraps around when reaching end of key
    result = ""
    for letter in text:
        if letter in alphabet: #checks if lowercase letter (in 'alphabet' dictionary)
            #convert plaintext to numeric value (0-25), add corresponding number of key letter,
            #take sum mod26, then convert back to char 
            ciph = chr(97 + (alphabet[letter] + alphabet[Key[count].lower()]) % 26) 
            result += ciph #append encrypted character
            count += 1
        elif letter in Alphabet: #same process but uppercase
            ciph = chr(65 + (Alphabet[letter] + alphabet[Key[count].lower()]) % 26) 
            result += ciph
            count += 1
        else: #non-alphabet character; leave it unchanged and do not increment key counter
            result += letter
        if count >= len(Key): #reset key counter if necessary
            count = 0
    return result

def decrypt(text, Key):
    count = 0 #tracks current position in Key; wraps around when reaching end of key
    result = ""
    for letter in text:
        if letter in alphabet: #lowercase
            #decrypt letter using current key character, subtract key value 
            #from cipher value, add 26 to avoid negatives, take modulo 26,
            # and convert back to lowercase.
            plain = chr(97 + (26 + alphabet[letter] - alphabet[Key[count].lower()]) % 26) 
            result += plain #append plaintext
            count += 1
        elif letter in Alphabet: #same process but uppercase
            plain = chr(65 + (26 + Alphabet[letter] - alphabet[Key[count].lower()]) % 26)
            result += plain
            count += 1
        else: #non-alphabet character; leave it unchanged
            result += letter
        if count >= len(Key):
            count = 0
    return result

def user(Key): #read user input and direct to either encryption/decryption with Key in tow
    try:
        while True:
            line = input()
            if sys.argv[1] == "-d":
                print(decrypt(line, Key))
            elif sys.argv[1] == "-e":
                print(encrypt(line, Key))
    except EOFError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

def wrong():
    print("Run file using: -e for encryption or -d for decryption followed by Key.")
    sys.exit(0)


alphabet = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)} #dictionary to map letters to numbers (lowercase)
Alphabet = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)} #dictionary to map letters to numbers (uppercase)
if len(sys.argv) == 3: #checks that all 3 arguments were provided in cmd line
    if sys.argv[1] in ("-d", "-e"): #checks for encypt/decrypt
        key = "".join(sys.argv[2].split()) #remove spaces from provided key
        user(key)
    else:
        wrong()
else:
    wrong()
