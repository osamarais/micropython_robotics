import numpy as np
import cv2
import time
import aruco_dedector_lib as arli
import math

dedector= arli.ArucoDedector()    
     

    

def introbot(intpos,first,second):


	robdis=((intpos[second][0]-intpos[first][0])**2+(intpos[second][1]-intpos[first][1])**2)**0.5

	robangle=180/math.pi*math.atan2(intpos[second][1]-intpos[first][1],intpos[second][0]-intpos[first][0])


	robangle=-90+(-90-robangle)
	if robangle<0:
		robangle+=360

	print(robdis,robangle)

	return robdis,robangle





def inourout(mar,pos,robpos,xmin,first,second):


	while True:
		dedector.Update()
	    
		X15, Y15, A15 = dedector.Locate(15)
		X11, Y11, A11 = dedector.Locate(11)
		X5, Y5, A5 = dedector.Locate(5)
		X10, Y10, A10 = dedector.Locate(10)
		X16, Y16, A16 = dedector.Locate(16)
		X6, Y6, A6 = dedector.Locate(6)

		if not None in (X15, X11, X5, X10, Y16, X6):
			break





	l=len(pos)
	a=l*[0]
	c=l*[0]
	root=l*[0]
	dis=l*[0]
	r=l*[0]
	mindis=l*[0]
	polvec=l*[0]
	pointvec=l*[0]
	xval=l*[0]
	magpol=l*[0]
	magpoint=l*[0]
	closepoint=l*[0]


	for i in range(l):
		if i==l-1:
			i=-1
		polvec[i]=[pos[i+1][0]-pos[i][0],pos[i+1][1]-pos[i][1]]      #(p2-p1)

		pointvec[i]=[robpos[0]-pos[i][0],robpos[1]-pos[i][1]]        #(p0-p1)

		r[i]=(polvec[i][0]*pointvec[i][0]+polvec[i][1]*pointvec[i][1])/((polvec[i][0])**2+(polvec[i][1])**2)


		
		magpol[i]=((pos[i+1][0]-pos[i][0])**2+(pos[i+1][1]-pos[i][1])**2)**0.5

		magpoint[i]=((robpos[0]-pos[i][0])**2+(robpos[1]-pos[i][1])**2)**0.5

		if r[i]>1:
			mindis[i]=((robpos[0]-pos[i+1][0])**2+(robpos[1]-pos[i+1][1])**2)**0.5
			closepoint[i]=pos[i+1]
			
		elif r[i]<0:
			mindis[i]=((pointvec[i][0])**2+(pointvec[i][1])**2)**0.5
			closepoint[i]=pos[i]
		else:
			mindis[i]=(abs((pointvec[i][0])**2+(pointvec[i][1])**2-(r[i])**2*(magpol[i])**2)**0.5)
			closepoint[i]=[pos[i][0]+r[i]*(pos[i+1][0]-pos[i][0]),pos[i][1]+r[i]*(pos[i+1][1]-pos[i][1])]
	countpass=0

	print(mindis)

	for j in range(l):

		if j==l-1:
			j=-1

		if pos[j][1]<robpos[1]<pos[j+1][1] or pos[j+1][1]<robpos[1]<pos[j][1]:

			xval[j]=pos[j][0]+(robpos[1]-pos[j][1])/((pos[j+1][1]-pos[j][1])/(pos[j+1][0]-pos[j][0]))

			if xmin<xval[j]<robpos[0]:
				countpass+=1



	if countpass%2==1:
		print("in")

	if countpass%2==0:
		print("out")

	print(min(mindis))

	countmin=0
	for mi in mindis:
		if mi==min(mindis):
			break
		countmin+=1

	direction=[robpos[1]-closepoint[countmin][1],robpos[0]-closepoint[countmin][0]]

	angle=180/math.pi*math.atan2(direction[0],direction[1])

	angle=90+90-angle

	print(angle)



	introbot(pos,first,second)

	return mindis


    
while True:


	while True:
		dedector.Update()
	    
		X15, Y15, A15 = dedector.Locate(15)
		X11, Y11, A11 = dedector.Locate(11)
		X5, Y5, A5 = dedector.Locate(5)
		X10, Y10, A10 = dedector.Locate(10)
		X16, Y16, A16 = dedector.Locate(16)
		X6, Y6, A6 = dedector.Locate(6)

		if not None in (X15, X11, X5, X10, Y16, X6):
			break





	mar=[10,12,16,18,24]
	pos=[[X5,Y5],[X10,Y10],[X11,Y11],[X15,Y15],[X16,Y16]]
	robpos=[X6,Y6]

	xmin=min(pos[:][0])-(max(pos[:][0])-min(pos[:][0]))*0.1




	t0 = time.time() 

	
	inourout(mar,pos,robpos,xmin,1,3)

	print("time passed: {}".format(time.time()-t0))

