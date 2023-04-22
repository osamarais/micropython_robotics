def parsedata(sock):
	while 1:
		try:
			data = readsock(sock)
			if data == 'exit loop':
				break
			elif type(data)==tuple and len(data)==3:
				LED(1024*data[0],1024*data[1],1024*data[2])
				print('got LED data')
			else:
				print('unknown data instead of LED data')
		except OSError:
			print('Timed out')
		except KeyboardInterrupt:
			print('Exiting Loop')
			break

	print('now waiting for robot data')
	while 1:
		try:
			data = readsock(sock)
			if data == 'exit loop':
				break
			elif type(data)==tuple and len(data)==3:
				print('got robot data')
			else:
				print('unknown data instead of robot data')
		except OSError:
			print('Timed out')
		except KeyboardInterrupt:
			print('Exiting Loop')
			break
