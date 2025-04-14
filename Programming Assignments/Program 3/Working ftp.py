from ftplib import FTP

HOST = ""
DIR = "/"
USER = ""
PASS = ""
METHOD = 7
PASSIVE = True

files = []

ftp = FTP()
ftp.connect(HOST)
ftp.login(USER, PASS)

ftp.set_pasv(PASSIVE)

ftp.dir(DIR, files.append)
ftp.quit()


def crack(text, n):
    count = 0    
    cur = 0
    message = ""
    for letter in text:
        if count > n:
            message += chr(cur)
            cur = 0
            count = 0
        if letter == "1":
            cur += 2 ** (n - count)
        count += 1
    message += chr(cur)
    return message



message = ""
for file in files:
    binary = ""
    for letter in file[0:10]:
        if letter == "-":
            binary += "0"
        else:
            binary += "1"
    
    if METHOD == 7 and binary[:3] == "000":
        binary = binary[3:]
        message += crack(binary, 6)

    elif METHOD == 10:
        message += crack(binary, 9)


print(message) 
