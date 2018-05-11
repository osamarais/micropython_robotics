import servolib
import math






class robot(servolib.continuousservo):
	"""

	Initializes the robot with its three continuous servo motors

	"""

	def __init__(self):

		# Three motors initialized
		self._front = servolib.continuousservo(5)
		self._right = servolib.continuousservo(4)
		self._left = servolib.continuousservo(0)

	# This method will translate the robot with the given
	# speed (-100 to 100),
	# runtime (in ms),
	# heading in degrees clockwise
	def translate(self, speed = 0 , runtime = 0, heading = 0):
		## Scale speed to account for trigonometry
		#speed = speed / math.cos(math.radians(60))
		self._front.speed =  int( speed * math.sin(math.radians(heading))		)
		self._right.speed =  int( speed * math.sin(math.radians(heading + 240))	)
		self._left.speed =   int( speed * math.sin(math.radians(heading + 120))	)

		self._front.runtime = runtime
		self._right.runtime = runtime
		self._left.runtime = runtime



	def runrobot(self):
		servolib.continuousservo.runallmotors()