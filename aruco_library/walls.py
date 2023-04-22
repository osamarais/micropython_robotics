##
#!/usr/bin/python3
"""
Created on Thu May 10 16:43:30 2018

@author: Alper
"""
import time
import numpy as np
import cv2
import aruco_dedector_lib as arli

MARKER_SIDE_LENGHT = 0.3 # meters

RESERVED_COLOR_WALL = (0, 0, 250) # reserved color for walls 




def IdToCenterLoacation(ID, liste):
    for k in range(10):
        for i, element in enumerate(liste[1]):
            if element == ID:
                return(liste[2][i], liste[3][i])
                
    return (None, None)

class CornerStone:  #class of our map
    
    _objs = []
    
    def __init__(self, ID, dedector):
        self.ID = ID
        print ("init"+str(ID))
        self.centerLoacation = (None, None)
        
        while self.centerLoacation == (None, None):
            cv2.waitKey(20)            
            self.centerLoacation = IdToCenterLoacation(ID, dedector.Locations) #center location of element
            if self.centerLoacation == (None, None):
                dedector.Locate()
        
        CornerStone._objs.append(self)
        
    @classmethod
    def Update(cls, liste):    
        for obj in cls._objs:
            try:
                obj.centerLoacation = IdToCenterLoacation(obj.ID, liste) #center location of element
            except TypeError:
                pass
        

class Wall:
    
    _objs = []
    
    def __init__(self, ID_1, ID_2, dedector):
        print("initilize wall")
        self.master = CornerStone(ID_1, dedector)
        print("master initilized")
        self.slave = CornerStone(ID_2, dedector)
        print("slave initilized")
        
        self.X1, self.Y1 = self.master.centerLoacation
        self.X2, self.Y2 = self.slave.centerLoacation
                
        Wall._objs.append(self)
    
    @classmethod
    def draw_wall(cls,img):  
        for obj in cls._objs:

            cv2.line(img, (obj.X1, obj.Y1), (obj.X2, obj.Y2), RESERVED_COLOR_WALL, 6)

        return True
    
        
    @classmethod
    def Update(cls, liste):
        for obj in cls._objs:
            obj.master.Update(liste)
            obj.slave.Update(liste)
            if not obj.master.centerLoacation == (None, None):
                obj.X1, obj.Y1 = obj.master.centerLoacation
            if not obj.slave.centerLoacation == (None, None):
                obj.X2, obj.Y2 = obj.slave.centerLoacation
             
             
    
if __name__ == "__main__":
    
    dedector= arli.ArucoDedector()
    debug = __name__ == "__main__"
    debug = dedector.show()   
    cv2.waitKey(1000)
    
    wait = False
    while not wait:
        wait = dedector.Locate()[0]
    
    print(dedector.Locations)
   
    Wall_0 = Wall(10,11, dedector)
    Wall_1 = Wall(11,16, dedector)
    Wall_2 = Wall(16,15, dedector)
    Wall_3 = Wall(15,10, dedector)

    
    while debug :
        t0 = time.time()
        dedector.Locate()

        Wall.draw_wall(dedector.frame)
        print("draw")
        debug = dedector.show()
        print("show")
        Wall.Update(dedector.Locations)
        print("Update")
        
        t1 = time.time()
        total = t1-t0
        print("time passed: {}".format(total))
    
    dedector.kill()    
        
