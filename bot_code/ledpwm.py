import machine


def LED(red,green,blue):
	# create the pin objects for the LEDs
	#r = machine.Pin(12)#6
	#g = machine.Pin(14)#5
	#b = machine.Pin(2)#4
	r = machine.Pin(14)#5
	g = machine.Pin(12)#6
	b = machine.Pin(13)#7
	# create PWM objects
	r = machine.PWM(r,50,int(1024-red))
	g = machine.PWM(g,50,int(1024-green))
	b = machine.PWM(b,50,int(1024-blue))


