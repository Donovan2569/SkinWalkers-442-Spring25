import socket
from sys import stdout
from time import time


ip = "138.47.99.228"
port = 31337

DEBUG = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

data = s.recv(4096).decode()
binary = ""
print("[connect to the chat server]\n...")
while data.rstrip("\n") != "EOF":
        stdout.write(data)
        stdout.flush()

        t0 = time()
        data = s.recv(4096).decode()
        t1 = time()

        delta = round(t1 - t0, 3)
        # NEED TO FIGURE OUT WHAT THE DELAY FOR 0 IS #
        # NEED TO FIGURE OUT WHAT THE DELAY FOR 1 IS #
        if delta == 1:  
            binary += "0"
        else:
            binary += "1"

        if DEBUG:
            stdout.write(f" {delta}\n")
            stdout.flush()

s.close()
print("...\n[disconnect from the chat server]")
print(binary)
