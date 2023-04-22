#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:32:33 2018

@author: mechastu
"""
import aruco_dedector_lib as arli
import random
import socket
import time
import numpy as np


dedector = arli.ArucoDedector(0)

UDP_IP = "192.168.1.116"
UDP_PORT = 8005
MESSAGE = b"Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP


loop = True
while loop:
    loop = dedector.show()
    dedector.Update()
    print("shape",dedector.frame[:,:,0].shape)
    
    
    for i in  range(len(dedector.frame[0,:,0])):
        MESSAGE = dedector.frame[:,i,0] #[random.randint(0,100)]
        MESSAGE = list(MESSAGE)
        MESSAGE.append(i)
        MESSAGE = str(MESSAGE)

        print ("message:", np.array(MESSAGE))
        MESSAGE = bytes( MESSAGE, 'utf-8')
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        time.sleep(0.1)