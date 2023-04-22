
# set up the socket
import socket
import random


# function to send data
def senddata(data,IP,port,sock):
	data = str(data)
	data = bytes(data,'utf-8')
	port = int(port)
	sock.sendto(data,(IP,port))


# function to broadcast data
def broadcastpositions():
	# get broadcastableobjects
	broadcastableobjects = [x for x in category.instances if x.broadcastable]
	# for each broadcastable object find the objects we need to broadcast
	broadcastableobjectscansee = [x.cansee for x in broadcastableobjects]
	# now find these objects in all the objects
	broadcastableobjectstobroadcast = [[[x for x in category.instances if x.name == y][0] for y in z] for z in broadcastableobjectscansee]
	# now we need to create the info to broadcast
	# create sublists of the IDs of the members we are broadcasting
	broadcastableobjectstobroadcastIDs = [[x.members for x in y] for y in broadcastableobjectstobroadcast]
	# convert to integers
	broadcastableobjectstobroadcastIDs = [[[int(x) for x in y] for y in z] for z in broadcastableobjectstobroadcastIDs]
	# get the coordinates of these IDs
	Locations = [[[d.Locate(x) for x in y] for y in z] for z in broadcastableobjectstobroadcastIDs]
	# trim the location float to a certain precison if necessary
	# send the data of broadcastable objects to the correct IP
	[ senddata( Locations[x[0]] , str.split(broadcastableobjects[x[0]].IP,':')[0] , str.split(broadcastableobjects[x[0]].IP,':')[1] , sock ) for x in enumerate(broadcastableobjects)]

def broadcastLEDsync():
	broadcastableobjects = [x for x in category.instances if x.broadcastable]
	randomLEDPWM = (random.random(),random.random(),random.random())
	print(randomLEDPWM)
	[ senddata( randomLEDPWM , str.split(broadcastableobjects[x[0]].IP,':')[0] , str.split(broadcastableobjects[x[0]].IP,':')[1] , sock ) for x in enumerate(broadcastableobjects)]

def broadcastmessage(message):
	[ senddata( message , str.split(broadcastableobjects[x[0]].IP,':')[0] , str.split(broadcastableobjects[x[0]].IP,':')[1] , sock ) for x in enumerate(broadcastableobjects)]


#def updateview():
#	rgbImage = cv2.cvtColor(d.frame, cv2.COLOR_BGR2RGB)
#	convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
#	p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#	pixmap = QPixmap.fromImage(p)
#	mainwindow.ui.camera_view.setPixmap(pixmap)



