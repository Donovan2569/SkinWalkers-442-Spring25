import sys
alphabet = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)} # dictionary to map letters to numbers (lowercase)
Alphabet = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)} # dictionary to map letters to numbers (uppercase)

def wrong():
    print("Run file using: -e for encryption or -d for decryption followed by Key.")
    exit()
    
def encrypt(text, Key):
    count = 0
    res = ""
    for letter in text:
        if count >= len(Key):
            count = 0
        if letter in alphabet and Key[count].lower() in alphabet:
            ciph = chr(97 + (alphabet[letter] + alphabet[Key[count].lower()]) % 26)
        elif letter in Alphabet and Key[count].lower() in alphabet:
            ciph = chr(65 + (Alphabet[letter] + alphabet[Key[count].lower()]) % 26)
        else:
            ciph = letter
        res += ciph
        count += 1
    return res

def decrypt(text, Key):
    count = 0
    res = ""
    for letter in text:
        if count >= len(Key):
            count = 0
        if letter in alphabet and Key[count].lower() in alphabet:
            plain = chr(97 + (26 + alphabet[letter] - alphabet[Key[count].lower()]) % 26)
        elif letter in Alphabet and Key[count].lower() in alphabet:
            plain = chr(65 + (26 + Alphabet[letter] - alphabet[Key[count].lower()]) % 26)
        else:
            plain = letter
        res += plain
        count += 1
        
    return res

def user(Key):
    while True:
        try:
            usrInput = input()
            if sys.argv[1] == "-d":
                print(decrypt(usrInput, Key))
            
            elif sys.argv[1] == "-e":
                print(encrypt(usrInput, Key))
        
        # Exit program when End of File is reached
        except EOFError:
            sys.exit(0)
                
        # exit program when interrupted without throwing an error
        except KeyboardInterrupt:
            sys.exit(0)


if len(sys.argv) == 3: # checks that all 3 arguments were provided in command line
    if sys.argv[1] == "-d" or sys.argv[1] == "-e": # checks for encypt/decrypt
        user(sys.argv[2]) # the key
    else:
        wrong()
