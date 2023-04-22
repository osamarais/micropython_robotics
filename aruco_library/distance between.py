import numpy as np
import cv2
import time
import aruco_dedector_lib as arli
import math

dedector= arli.ArucoDedector()    
     


    
while True:


	while True:
		dedector.Update()

		X16, Y16, A16 = dedector.Locate(16)
		X6, Y6, A6 = dedector.Locate(6)

		if not None in (Y16, X6):
			break



	t0 = time.time() 

	
	print("distance: {}".format(math.sqrt((X6-X16)**2+((Y6-Y16)**2))))
	print("time passed: {}".format(time.time()-t0))

