import socket

UDP_IP = "192.168.1.114"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

  # buffer size is 1024 bytes
sock.recv(1024)