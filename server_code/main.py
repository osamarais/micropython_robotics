# configuration parameters

# camera parameters


MARKER_SIDE_LEN = 0.04
NUM_OF_TRIALS = 10
camera_port = 1


# load libraries
exec(open("UI.py").read())
exec(open("aruco_dedector_lib.py").read())
exec(open("broadcastlib.py").read())

# create the camera detector object
d = ArucoDedector(camera_port, False)
d.Update()
allmarkers = d.list_ID()
allmarkers = [str(x) for x in allmarkers]

# initialize unidentified category
category('unidentified')
update_unidentified_category()
update_categories_list()

# create the socket object
sock = socket.socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)





import time


print('waiting for setup')
# wait till setup is complete
while 1:
	try:
		d.Update()
		d.show()
	except KeyboardInterrupt:
		break


		
	except:
		pass


#print('sending LED sync message')
## send the LED colors to see if everything is synchronized
#while 1:
#	try:
#		time.sleep(0.5)
#		d.Update()
#		d.show()
#		broadcastLEDsync()
#	except KeyboardInterrupt:
#		broadcastmessage('exit loop')
#		break
#	except:
#		pass
#
#
#print('sending start message')
#broadcastmessage('start')
#
#
## over here create the loop for sending data continuously
#print('broadcasting positions')
#while 1:
#	try:
#		d.Update()
#		d.show()
#		broadcastpositions()
#	except KeyboardInterrupt:
#		break
#	except:
#		pass
while 1:
	try:
		d.Update()
		broadcastpositions()
		d.show()
		
	except:
		break
