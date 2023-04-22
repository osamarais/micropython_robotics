from math import atan2, degrees, sqrt

def follow(number):
	# make the robot go to the correct marker ID

#	# first Light up the LEDs while waiting for the start command
#	while 1:
#		try:
#			data = readsock(sock)
#			if data == 'exit loop':
#				break
#			elif type(data)==tuple and len(data)==3:
#				LED(1024*data[0],1024*data[1],1024*data[2])
#				print('got LED data')
#			else:
#				print('unknown data instead of LED data')
#		except OSError:
#			print('Timed out')
#		except KeyboardInterrupt:
#			print('Exiting Loop')
#			break

	print('now waiting for robot data')
	while 1:
		try:
			data = readsock(sock)
			if data == 'exit loop':
				break
			elif type(data)==list and len(data)==2:
				print('got robot data')
				robot1, follow = data
				robot1 = robot1[0]
				follow = follow[number]
				x_slip = follow[0]-robot1[0]
				y_slip = follow[1]-robot1[1]
				heading = degrees(atan2(y_slip,x_slip))
				orientation = robot1[2]
				print('heading to {0}'.format(heading))
				#maybe add PID here
				distance = sqrt(x_slip**2 + y_slip**2)
				r.translate(int(mypid.controlcommand(distance)),200,heading,orientation)
				r.runrobot()
				print('gave command')
				# now use this data to run our robot
			else:
				print('unknown data instead of robot data')
		except OSError:
			print('Timed out')
			r.stoprobot()
		except KeyboardInterrupt:
			print('Exiting Loop')
			r.stoprobot()
			break
		except:
			print('exception !!')
			r.stoprobot()

def calibrate():
	while 1:
		try:
			data = readsock(sock)
			data = readsock(sock)
			if data == 'exit loop':
				break
			elif type(data)==list and len(data)==2:
				print('got robot data')
				robot1, follow = data
				robot1 = robot1[0]
				r.calibratebegin()
				data = readsock(sock)
				data = readsock(sock)
				robot2, follow = data
				robot2 = robot2[0]
				r.calibrateend(robot1[0], robot1[1], robot2[0], robot2[1], robot1[2], robot2[2])
				print('calibrated')
				break
				# now use this data to run our robot
			else:
				print('unknown data instead of robot data')
		except OSError:
			print('Timed out')
		except KeyboardInterrupt:
			print('Exiting Loop')
			r.stoprobot()
			break