import socket
from sys import stdout
from time import time

ip = "138.47.99.228"
port = 31337

DEBUG = True
THRESHOLD = 0.1  # You'll change this after analyzing delays

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

print("[connect to the chat server]\n...")

binary = ""
delays = []

data = s.recv(4096).decode()

while data.rstrip("\n") != "EOF":
    stdout.write(data)
    stdout.flush()

    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)
    delays.append(delta)

    # Interpret binary from delay
    if delta < THRESHOLD:
        binary += "0"
    else:
        binary += "1"

    if DEBUG:
        stdout.write(f" {delta}\n")
        stdout.flush()

s.close()

print("...\n[disconnect from the chat server]")

# Optional: print collected delay values to find your threshold
print("Collected Delays:", delays)

# Convert binary to ASCII
covert = ""
for i in range(0, len(binary), 8):
    byte = binary[i:i+8]
    if len(byte) == 8:
        covert += chr(int(byte, 2))

print(f"Covert message: {covert}")
