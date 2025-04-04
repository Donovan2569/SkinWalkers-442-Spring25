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
                        
                print("Permissions:", file[:10])  # Debug: Print extracted permissions
                print("Binary Representation:", perms)  # Debug: Print converted binary string
                
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
                    
    print("Final Binary String:", binary)  # Debug: Print full binary string before conversion
    
    # Convert binary to ASCII
    message = ""
    bit_size = 7 if METHOD == 7 else 8  # Ensure correct bit chunking
    for i in range(0, len(binary), bit_size):
        byte = binary[i:i+bit_size]
        if len(byte) == bit_size:
            num = int(byte, 2)
            message += chr(num)
    
    print("Decoded Message:", message.strip())  # Debug: Final decoded message
    
except KeyboardInterrupt:
    print("\nProgram interrupted by user")
