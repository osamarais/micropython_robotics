import numpy as np
import cv2
import time
import aruco_dedector_lib as arli
import math



dedector= arli.ArucoDedector()

Rbound=0.025
Rrobot=0.028


dedector.Update()


first=0
second=1      #WITH THESE TWO, WE CAN SPECIFY WHICH OF THE TWO ROBOTS WE ARE DEALING WITH TO GET DISTANCE ANGLE ETC...


#from text file get marker values for robots and boundaries
boundlist=[7,8,12,18,22]
roblist=[6,11]








l=len(boundlist)
lr=len(roblist)


def robdata(lr):
	
	aru=0
	robpos=[[0,0,0]]

	for li in range(lr-1):
		robpos.append([0,0,0])

	
	for aru in range(lr):
		#print(roblist[aru])
		#print("roblis aru", dedector.Locate(roblist[aru]))
		a1=roblist[aru]

		robpos[aru][0], robpos[aru][1], robpos[aru][2]= dedector.Locate(a1)
		#value of the markers on the robots should be given in a list like [3,8,12,1] means four robots and
		#these markes are on each of them. This function creates a list of 3*lr and this list contains all the
		#markers' position in x and y direction and orientation data.
		#
		#


	#print(robpos)

	return robpos

def bounddata(l):
	edge=0
	pos=[[0,0,0]]


	for li1 in range(l-1):
		pos.append([0,0,0])
	
	for edge in range(l):
		pos[edge][0], pos[edge][1], pos[edge][2]= dedector.Locate(boundlist[edge])
	#boundlist gives the position and orientation of markers at the edges of the polygons in a list like
	#[5,12,15,18,2,1,3,20] this is an octagon for example. also polygon starts with marker 5 and continues
	#like 12,15 and lastly it come back to 5 after marker 20. There may be more than one polygon so, numboun
	#specifies which one is chosen.
	#print(pos[1])
	return pos


def introbot(lr):

	dismat=[[0]*lr]*lr
	angmat=[[0]*lr]*lr

	intpos=robdata(lr)


	#these for loops gives the distance and angle between all robots as a list. later user can call it as dismat[0][1] etc...

	for intr in range(lr):
		for intr2 in range(lr):
			if intr!=intr2:
				dismat[intr][intr2]=((intpos[intr2][0]-intpos[intr][0])**2+(intpos[intr2][1]-intpos[intr][1])**2)**0.5

				angmat[intr][intr2]=math.degrees(math.atan2(intpos[intr2][1]-intpos[intr][1],intpos[intr2][0]-intpos[intr][0]))
				#angmat[intr][intr2]=(angmat[intr][intr2])
				if angmat[intr][intr2]<0:
					angmat[intr][intr2]+=360
	#print(dismat[0][1],angmat[0][1])
	return dismat,angmat


def inourout(boundlist,lr,numrobot):

	while True:
		dedector.Update()
	    
		"""X15, Y15, A15 = dedector.Locate(15)
		X11, Y11, A11 = dedector.Locate(11)
		X5, Y5, A5 = dedector.Locate(5)
		X10, Y10, A10 = dedector.Locate(10)
		X16, Y16, A16 = dedector.Locate(16)
		X6, Y6, A6 = dedector.Locate(6)"""


		c1=len(roblist)*[[0]*3]
		c2=len(roblist)*[[0]*3]

		for check in range(len(roblist)):
			c1[check][0],c1[check][1],c1[check][2]=dedector.Locate(roblist[check])

		for check2 in range(len(boundlist)):
			c2[check][0],c2[check][1],c2[check][2]=dedector.Locate(boundlist[check2])


		if not None in c1 and c2:


		#if not None in (X15, X11, X5, X10, Y16, X6):
			break

	"""xmin=99999999999

	for minx in range(len(boundlist)):
		if xmin>=boundlist[minx]:
			xmin=boundlist[minx]"""

	xmin=-5


	r=l*[0]
	mindis=l*[0]
	polvec=l*[0]
	pointvec=l*[0]
	xval=l*[0]
	magpol=l*[0]
	magpoint=l*[0]
	closepoint=l*[0]

	pos=bounddata(l)
	robposmat=robdata(lr)
	robpos=robposmat[numrobot]
	
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

	for j in range(l):

		if j==l-1:
			j=-1

		if pos[j][1]<robpos[1]<pos[j+1][1] or pos[j+1][1]<robpos[1]<pos[j][1]:

			xval[j]=pos[j][0]+(robpos[1]-pos[j][1])/((pos[j+1][1]-pos[j][1])/(pos[j+1][0]-pos[j][0]))

			if xmin<xval[j]<robpos[0]:
				countpass+=1


	if countpass%2==1:
		print("in")
		state=True

	if countpass%2==0:
		print("out")
		state=False


	countmin=0
	for mi in mindis:
		if mi==min(mindis):
			break
		countmin+=1

	direction=[robpos[1]-closepoint[countmin][1],robpos[0]-closepoint[countmin][0]]

	escangle=math.degrees(math.atan2(direction[0],direction[1]))
	if escangle<0:
		escangle+=360

	#escangle=90+90-escangle

	print(escangle)

	return mindis[countmin],state,countmin,escangle

	#first output of this function gives minimum distance between a specified robot and a polygon

	#second output gives True if robot is inside the polygon and False otherwise

	#third output gives which side closest point is in. for example if gives 3, closest point is in the side created by
	#3rd and 4th points. Also note that closest point may be on the 3rd or 4th point. it does not have to be between them.
	#fourth output gives the angle of the vector from robot to closest point on the polygon. For example, if angle 

	#is 60 degrees a vector from closest point to robot is 60 degrees which means robot can move in 60 degrees
	#direction to maximize the amount of speed of escape from that point. Because if robot go in the 
	#60+180=240 direction it will directly go into the wall of the polygon. 60 degree is exactly opposite of this.






indismat,inangmat=introbot(lr)      #initial distance and angle matrices between robots
indisrob=indismat[first][second]   	 #initial distance and angle between specified robots
inangrob=inangmat[first][second]
#print(inangrob)
if inangrob<0:
	inangrob+=360


inedgepos=bounddata(l)     #coordinates of boundaries
inrobpos=robdata(lr)       #positions of the robots in a list



#to get the angle between prey and each of the corners:
bound_angle=[[0]*3]*l

for k in range(l):
	bound_angle[k]=math.degrees(math.atan2(inedgepos[k][1]-inrobpos[first][1],inedgepos[k][0]-inrobpos[first][0]))
	if bound_angle[k]<0:
		bound_angle[k]+=360
	if bound_angle[k]<0:
		bound_angle[k]+=360
	#if bound_angle[k]<180:
	#	bound_angle[k]+=360


#for kk in range(l):
	#if bound_angle[kk]>bound_angle[l-1]:
		#bound_angle[kk]-=360

countmax=0
for maxx in range(l):
	if bound_angle[maxx]==min(bound_angle):
		break
	countmax+=1


#print(bound_angle)

pas=0

for m in range(l):
	if m==l-1:
		m=-1

	if bound_angle[m]>inangrob>bound_angle[m+1]:
		break
	pas+=1

if pas==l:
	pas=countmax

#print(pas,bound_angle,inangrob)
#for example, if the pas is 3, passage is between 3rd and 4th elements in the list.

bodis=inedgepos       #coordinates of boundaries
aa=0

for n in range(int(l/2)+1):

	if ((bodis[(pas+1+n)%l][0]-bodis[(pas+n)%l][0])**2+(bodis[(pas+1+n)%l][1]-bodis[(pas+n)%l][1])**2)**0.5>3*Rrobot+2*Rbound:
		aa=1
		break

	elif ((bodis[(pas+1-n)%l][0]-bodis[(pas-n)%l][0])**2+(bodis[(pas+1-n)%l][1]-bodis[(pas-n)%l][1])**2)**0.5>3*Rrobot+2*Rbound:
		aa=-1
		break

passage=(pas+n*aa)%l
if passage==l-1:
	passage=-1



#passage boundaries

avgaim=[(inedgepos[passage][0]+inedgepos[passage+1][0])/2,(inedgepos[passage][1]+inedgepos[passage+1][1])/2]
angaim=math.atan2(inedgepos[passage+1][1]-inedgepos[passage][1],inedgepos[passage+1][0]-inedgepos[passage][0])-math.pi/2
aim=[avgaim[0]+Rrobot*math.cos(angaim),avgaim[1]+Rrobot*math.sin(angaim)]


#print(math.degrees(angaim))


preycount=0

if passage==-1:
	passage=l-1
#print(passage)



#BURDAN SONRASI LOOP İÇİNDE DÖNME OLAYI
while True:

	while True:
		dedector.Update()



		c1=len(roblist)*[[0]*3]
		c2=len(roblist)*[[0]*3]

		for check in range(len(roblist)):
			c1[check][0],c1[check][1],c1[check][2]=dedector.Locate(roblist[check])

		for check2 in range(len(boundlist)):
			c2[check][0],c2[check][1],c2[check][2]=dedector.Locate(boundlist[check2])


		if not None in c1 and c2:
		#if not None in (X15, X11, X5, X10, Y16, X6):
			break

	"""mar=[10,12,16,18,24]
	pos=[[X5,Y5],[X10,Y10],[X11,Y11],[X15,Y15],[X16,Y16]]
	robpos=[X6,Y6]

	xmin=min(pos[:][0])-(max(pos[:][0])-min(pos[:][0]))*0.1"""



	robpos=robdata(lr)
	preypos=robpos[second]
	predpos=robpos[first]

	if preycount==0:
		preyangle=math.degrees(math.atan2(aim[1]-preypos[1],aim[0]-preypos[0]))

	else:
		preyangle=(math.degrees(angaim)+180)%360

	if preyangle<0:
		preyangle+=360

	print(preyangle)

	if ((preypos[0]-aim[0])**2+(preypos[1]-aim[1])**2)**0.5<Rrobot*0.5:
		preycount+=1


	#print(math.degrees(angaim))
	predangle=math.degrees(math.atan2(preypos[1]-predpos[1],preypos[0]-predpos[0]))

	#print(predangle)

	#robdata(lr)
	#bounddata(l)
	#introbot(lr)
	#inourout(boundlist,lr,first)


	#t0 = time.time()

	#print("time passed: {}".format(time.time()-t0))