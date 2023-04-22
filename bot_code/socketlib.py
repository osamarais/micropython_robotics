import socket
import network




def ip(wlan):
	return wlan.ifconfig()


def UDP(wlan,port):
	UDP_IP = ip(wlan)[0]
	UDP_PORT = 8001
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind((UDP_IP, UDP_PORT))
	sock.settimeout(2)
	return sock


def readsock(sock):
	data = sock.recv(1024).decode("utf-8") # buffer size is 1024 bytes
	return eval(data)
