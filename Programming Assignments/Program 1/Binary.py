import sys
# Decode a binary string into readable text
def crack(text, n):
    res = ""
    cur = 0
    count = 0
    for letter in text:
        if count > n:
            res += chr(cur)
            cur = 0
            count = 0
        if letter == "1":
            cur += 2 ** (n - count)
        
        count += 1
    res += chr(cur)
    return res

# Get the input from the user
file = sys.stdin.read()
file = file.strip("\n")

# Determine whether the file is 8 or 7 bit then decode
if len(file) % 8 == 0:
    print("8 bit: " + crack(file, 7))

elif len(file) % 7 == 0:
    print("7 bit: " + crack(file, 6))
