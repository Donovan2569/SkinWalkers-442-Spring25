# Program 3: FTP Covert Channel
# CSC 442: Intro to Cybersecurity - Group 4
# 4/4/25

import ftplib

FTP_HOST = "138.47.99.229"  # FTP server address
FTP_PORT = 21
FTP_DIR = "/"  # Target directory
METHOD = 7  # Set METHOD to 7 for 7-bit method, 10 for 10-bit method

#Username and Password
user = "percypatterson"
password = "himalayas"

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(user, password)
    files = []
    ftp.dir(FTP_DIR, files.append)
    ftp.quit()
    
    binary = ""
    for file in files:
        # Check if line is long enough and has valid permissions
        valid = True
        if len(file) >= 10:
            for i in range(10):
                if file[i] not in '-rwx':
                    valid = False
                    break
            
            if valid:
                # Convert permissions to binary
                perms = ""
                for c in file[1:10]:
                    if c == '-':
                        perms += '0'
                    else:
                        perms += '1'
                
                # For 7-bit method, check if first three bits are all 0
                if METHOD == 7:
                    first_three_zero = True
                    for i in range(3):
                        if perms[i] == '1':
                            first_three_zero = False
                            break
                    if first_three_zero:
                        binary += perms[-7:]
                elif METHOD == 10:
                    binary += perms
    
    # Convert binary to ASCII
    message = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:  
            num = 0
            for j in range(8):
                if byte[j] == '1':
                    num += 2 ** (7-j)
            message += chr(num)
    
    print(message.strip())
    
except KeyboardInterrupt:
    print("\nProgram interrupted by user")
