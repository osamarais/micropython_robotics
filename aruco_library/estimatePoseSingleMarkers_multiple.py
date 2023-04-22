# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:37:29 2018

@author: Alper
"""

import numpy as np
import cv2
import time



def RotationVectorToEulerAngles_deg(Rotation) :
    
    R = cv2.Rodrigues(Rotation)[0]
 
     
    sy = np.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sy < 1e-6
 
    if  not singular :
        x = np.arctan2(R[2,1] , R[2,2])
        y = np.arctan2(-R[2,0], sy)
        z = np.arctan2(R[1,0], R[0,0])
    else :
        x = np.arctan2(-R[1,2], R[1,1])
        y = np.arctan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])*180/np.pi

font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 1
fontColor              = (255,255,0)
lineType               = 2

MARKER_SIDE_LEN = 0.03 #METERS

cameraMatrix = np.load("cam_broke_mtx.npy")
distCoeffs = np.load("cam_broke_dist.npy")

cap = cv2.VideoCapture(0)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    res = cv2.aruco.detectMarkers(gray,dictionary)
#   print(res[0],res[1],len(res[2]))
    cv2.aruco.drawAxis(frame, cameraMatrix, distCoeffs, (0,0,0), (0,0,0), 0.1)
    if len(res[0]) > 0:
        cv2.aruco.drawDetectedMarkers(frame,res[0],res[1])
    
    
    
    X = 0
    Y = 0
    Z = 0
    A0 = 0
    A1 = 0
    A2 = 0
    for i in res[0]:
        a=cv2.aruco.estimatePoseSingleMarkers(i, MARKER_SIDE_LEN, cameraMatrix, distCoeffs)
        cv2.aruco.drawAxis(frame, cameraMatrix, distCoeffs, a[0][0][0], a[1][0][0], 0.03)
        eulerAngles = RotationVectorToEulerAngles_deg(a[0][0][0]) 
        
        X += a[1][0][0][0]
        Y += a[1][0][0][1]
        Z += a[1][0][0][2]
        A0 += (180/np.pi*eulerAngles[0])
        A1 += (180/np.pi*eulerAngles[1])
        A2 += (180/np.pi*eulerAngles[2])
        
    LEN = len(res[0])
    if LEN:
            
        
        textX = ( "x: {}".format(X/LEN))
        textY = ( "y: {}".format(Y/LEN))
        textZ = ( "z: {}".format(Z/LEN))
        textA0 = ( "Angle: {}".format(A0/LEN))
        textA1 = ( "Angle: {}".format(A1/LEN))
        textA2 = ( "Angle: {}".format(A2/LEN))
    
        cv2.putText(frame, textX, (30 ,30), font, fontScale, fontColor, lineType)
    
        cv2.putText(frame, textY, (30 ,70), font, fontScale, fontColor, lineType)
    
        cv2.putText(frame, textZ, (30 ,110), font, fontScale, fontColor, lineType)
    
        cv2.putText(frame, textA0, (30 ,150), font, fontScale, fontColor, lineType)
        cv2.putText(frame, textA1, (30 ,190), font, fontScale, fontColor, lineType)
        cv2.putText(frame, textA2, (30 ,230), font, fontScale, fontColor, lineType)
        
        

    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


