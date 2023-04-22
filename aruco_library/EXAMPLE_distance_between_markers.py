#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:54:14 2018

@author: mechastu
"""
import time
import aruco_dedector_lib as arli
import math

dedector= arli.ArucoDedector()

contine = True
    
while contine:
    
        t0 = time.time()      

        
        dedector.Update()
        
        X15, Y15, A15 = dedector.Locate(15)
        X11, Y11, A11 = dedector.Locate(11)
        X5, Y5, A5 = dedector.Locate(5)
        X10, Y10, A10 = dedector.Locate(10)
        X16, Y16, A16 = dedector.Locate(16)
        X6, Y6, A6 = dedector.Locate(6)
        
        
#        
        mar=[5,10,11,15,16]
        pos=[[X5,Y5],[X10,Y10],[X11,Y11],[X15,Y15],[X16,Y16]]
        robpos=[X6,Y6]
        
        
        xmin=min(pos[:][0])-1
        
        def inourout(mar,pos,robpos):
            a=len(mar)*[0]
            c=len(mar)*[0]
            root=len(mar)*[0]
            dis=len(mar)*[0]
            
            
            
            for i in range(len(mar)):
            
                    a[i]=(pos[i][1]-pos[i-1][1])/(pos[i][0]-pos[i-1][0])
            	  c[i]=-(a[i]*pos[i][0]+pos[i][1])
            	  root[i]=-(c[i]+robpos[1])/a[i]
            
            	  dis[i]=abs((a[i]*robpos[0]+robpos[1]+c[i])/(a[i]**2+1)**0.5)
            
            for ro in range(len(mar)):
            	  count=0
                  if xmin<root[ro]<robpos[0]:
            		    count+=1
            if count%2==0:
            	  print("out")
            
            else:
            	  print("in")
            
            
            distance=min(dis[:])
            print(distance)
            return distance
            
        inourout(mar,pos,robpos)
                    
        
        
        if not None in (X15, Y15, A15, X11, Y11, A11):        
            distance = math.sqrt((X15-X11)**2+(Y15-Y11)**2)
        
        print ("distance: {}".format(distance))
        
        contine = dedector.show()        

        print("time passed: {}".format(time.time()-t0))
    
dedector.kill()