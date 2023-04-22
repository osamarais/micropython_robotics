# calibrate the robot


def prey():
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
			elif type(data)==list and len(data)==3:
				print('got robot data')
				aim, orien, inside = data
				print('heading to {0}'.format(aim))
				#maybe add PID here
				if inside:
					r.translate(27,200,aim,orien)
					r.runrobot()
				else:
					r.stoprobot()
					print(outside)
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
