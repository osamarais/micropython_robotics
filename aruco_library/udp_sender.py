import random
import socket
import time

UDP_IP = "192.168.1.116"
UDP_PORT = 8005
MESSAGE = b"Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP



while 1:
    time.sleep(0.5)
    MESSAGE = [random.randint(0,100)]
    print ("message:", MESSAGE)
    MESSAGE = bytes( MESSAGE)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))