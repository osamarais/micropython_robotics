# some stuff added for our robot

import time
import socket
from robotlib import *
from math import atan2, degrees
import machine

r = robot()

def read(sock):
    data = sock.recv(1024).decode("utf-8") # buffer size is 1024 bytes
    data = sock.recv(1024).decode("utf-8") # buffer size is 1024 bytes
    return eval(data)
    
def runn(r):
    
    speed = 27
    size = 20
    stime = 10
    
    
    UDP_IP = "192.168.1.114"
    UDP_PORT = 8000
    
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    
    
    
    while True:
        data = sock.recv(1024) # buffer size is 1024 bytes
        if data.decode("utf-8") == "start":
            print("started")
            break
        
    
    
    data = read(sock)
    print("got firstposition")
    
    r.position = data[0]
    r.translate(speed,1000,0)
    while not(r._front._runtime == 0):
        r.runrobot()
        time.sleep_ms(stime)
    
    r.runrobot()
    print("done moving")
    time.sleep_ms(1000)
    data = read(sock)
    
    print("got second position")
    

    
    
    x_slip = data[0][0] -r.position[0]
    y_slip = data[0][1] -r.position[1]
    
    ofset_angle = atan2(y_slip, x_slip)
    ofset_angle = degrees(ofset_angle)-data[0][2]
    
    print("offset angle",ofset_angle)
    print("waiting for data")
    
    
    
    while True:

        data = read(sock)
        r.position = data[0]
        print("position", r.position)
        targetPosition = data[1]
        print("targetPosition",targetPosition)
        print("offset angle",ofset_angle)
        x_slip = targetPosition[0] -r.position[0]
        y_slip = targetPosition[1] -r.position[1]

        wantotogoto = degrees(atan2(y_slip, x_slip))
        print ("wantotogoto",wantotogoto)
        
        angleCommand = wantotogoto - ofset_angle - r.position[2]
        print ("angleCommand",angleCommand)
        
        r.translate(speed,size,angleCommand)
        r.runrobot()
        print("chasing")


time.sleep_ms(2000)
r.runrobot()
