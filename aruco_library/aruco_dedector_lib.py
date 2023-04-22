# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:07:57 2018

@author: Alper
"""

import cv2
import numpy as np
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
 
    return np.array([x, y, -z])*180/np.pi



## Settings for text oout put on to pictures
font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 1
fontColor              = (255,255,0)
lineType               = 2


MARKER_SIDE_LEN = 0.04
NUM_OF_TRIALS = 10


class ArucoDedector():

    """Class of detection process
    Initiates camera capture
        Sets up camera paremeters
    can be run on debug mode

    Args:
        camera port: If multiple cameras are connected or program is not able to kill the prewious caprure instances then re- pulging the camera phisally increses the counter.
        
        debug:      Prints the debug values during run. 
                    


    Data:
        Locations:  the location of detecteed markers in the format of (flag, tag, x, y, az) where each element is a list
            
            flag: Bolean value. Ture if at least one marker detected
            tag:ID of the marker
            x, y, az : koordiantes

        
        haveSeen:    the location of past detecteed markers stored for NUM_OF_TRIALS, in the format of (flag, tag, x, y, az) where each element is a list
    
    Instance Methods:
        kill():      Kills the camera capture.

        Update():   reads from camera caprue and updates "haveseen" and "Locations" 
            returns: Locations

        Locate(ID): returns the positon data of given ID from "Locations". if marker is not seen looks it in "haveseen". If not in any list returns (none, none, none)

        list_ID():
            returns list of seen IDs           
            
        show(): displays frame of capture, returns true. If "q" is given then returns false.

                   



    Class Methods:
        runallmotors(): This will do run() for all the continuous servo objects.




    Please note that this shall modify any previous configuration of the pin.
    On the ESP8266 the pins 0, 2, 4, 5, 12, 13, 14 and 15 all support PWM.


    """

    def __init__(self, cameraPort=0, debug = False):
        self.cap = cv2.VideoCapture(cameraPort)
        
        self.Locations = []
        
        self.DEBUG = debug
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

        
        self.cameraMatrix = np.load("cam_broke_mtx.npy")
        self.distCoeffs = np.load("cam_broke_dist.npy")

        self.haveSeen = {}    

    ############### Camera settings ##############    

#        
#        self.cap.set(cv2.CAP_PROP_FPS, 30)
#        self.cap.set(cv2.CAP_PROP_EXPOSURE, 20)
#        self.cap.set(cv2.CAP_PROP_CONTRAST, 10)
#        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, 224)


##        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        ret, self.frame = self.cap.read()
        
        if self.DEBUG:
            print ("debug mode")
    
    def kill(self):
        if self.DEBUG:
            print ("killing")
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows() 
        
    def Update(self):        
        
        flag = False
        tag, x, y, az = [], [], [], []
        
        if self.DEBUG:
            print ("locating")
        
        ret, self.frame = self.cap.read()
        
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        cv2.aruco.drawAxis(self.frame, self.cameraMatrix, self.distCoeffs, (0,0,0), (0,0,0), 0.3)
        
        detectedMarkers = cv2.aruco.detectMarkers(gray, self.dictionary)
        
        flag = len(detectedMarkers[0]) > 0
        

        
        if flag:
            
            markerCorners =detectedMarkers[0]
            markerIDs = detectedMarkers[1]
            
            if self.DEBUG:
                
                cv2.aruco.drawDetectedMarkers(self.frame, markerCorners, markerIDs)
        
            
            for i, marker in enumerate(markerCorners) :

                a=cv2.aruco.estimatePoseSingleMarkers(marker, MARKER_SIDE_LEN, self.cameraMatrix, self.distCoeffs)
                cv2.aruco.drawAxis(self.frame, self.cameraMatrix, self.distCoeffs, a[0][0][0], a[1][0][0], 0.03)
                 
                
                X = a[1][0][0][0]
                Y = -a[1][0][0][1]
                
                eulerAngles = RotationVectorToEulerAngles_deg(a[0][0][0])

                if self.DEBUG:
                    
                    cv2.putText(self.frame, str(X)+", "+ str(Y)+", "+str(eulerAngles[2]), (100 ,100), font, fontScale, fontColor, lineType)
        
            
                if not markerIDs[i][0] in self.haveSeen:
                    self.haveSeen[markerIDs[i][0]] = [markerIDs[i][0], X, Y, eulerAngles[2], 0]
                else:
                    self.haveSeen[markerIDs[i][0]][1] =  X
                    self.haveSeen[markerIDs[i][0]][2] =  Y
                    self.haveSeen[markerIDs[i][0]][3] = eulerAngles[2]            

                
                tag.append(markerIDs[i][0])
                x.append(X)
                y.append(Y)
                az.append(eulerAngles[2])


        for element in self.haveSeen:
            if not element in tag:
                self.haveSeen[element][-1] = self.haveSeen[element][-1] +1
            


        
        todel = []
        for element, data in self.haveSeen.items():
            if self.DEBUG:
                print ("data is {}".format(data))
            if data[-1] > NUM_OF_TRIALS:
                todel.append(element)
        
        if self.DEBUG:
            print ("to del is {}".format(todel))

        for element in todel:
            del self.haveSeen[element]



        self.Locations = (flag, tag, x, y, az)
        
        return self.Locations
        
    def Locate(self, ID):
        try:
            for i, tag in enumerate(self.Locations[1]):
                if tag == ID:
                    return (self.Locations[2][i], self.Locations[3][i], self.Locations[4][i])

            if ID in self.haveSeen:
                (num,x,y,a,p) = self.haveSeen[ID]
                return (x,y,a)
            return (None, None, None)

        except IndexError:
            return (None, None, None)
                           

            

        return (None, None, None)


    def list_ID(self):
        return list(self.haveSeen.keys())
            
        
        
    
    def show(self):
        cv2.imshow('Camera View',self.frame)        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True
                   
    
    
#debug = __name__ == "__main__"
debug = False
if debug:

    dedector= ArucoDedector(0,debug)
    
    while debug:
        t0 = time.time() 
        dedector.Update() 
        debug = dedector.show()
        print (len(dedector.list_ID()))
        print (dedector.list_ID())
        

        print("time passed: {}".format(time.time()-t0))
    
    dedector.kill()