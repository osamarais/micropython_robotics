import servolib
import math
import time





class robot(servolib.continuousservo):
	"""

	Initializes the robot with its three continuous servo motors

	"""

	def __init__(self):

		# Three motors initialized
		self._front = servolib.continuousservo(5)
		self._right = servolib.continuousservo(4)
		self._left = servolib.continuousservo(0)
		self.runtime = 0
		self.anglecalibration = 0
		# maybe add some speed calibration too

	# This method will translate the robot with the given
	# speed (-100 to 100),
	# runtime (in ms),
	# heading in degrees clockwise
	def translate(self, speed = 0 , runtime = 0, heading = 0, orientation = 0):
		## Scale speed to account for trigonometry
		#speed = speed / math.cos(math.radians(60))
		self._front.speed =  int( speed * math.sin(math.radians(-heading + self.anglecalibration + orientation)))
		self._right.speed =  int( speed * math.sin(math.radians(-heading + self.anglecalibration + orientation + 240)))
		self._left.speed =   int( speed * math.sin(math.radians(-heading + self.anglecalibration + orientation + 120)))

		self._front.runtime = runtime
		self._right.runtime = runtime
		self._left.runtime = runtime
		self.runtime = runtime

	def rotate(self, speed = 0, runtime = 0):
		self._front.speed =  int(speed)
		self._right.speed =  int(speed)
		self._left.speed =   int(speed)

		self._front.runtime = runtime
		self._right.runtime = runtime
		self._left.runtime = runtime
		self.runtime = runtime

	def calibratebegin(self, speed = 50, runtime = 1000, heading = 0):
		# move the robot
		# import time if needed
		self.anglecalibration = 0
		self.translate(speed,runtime,heading,0)
		print('got info')
		while self.runtime > 0:
			self.runrobot()
			print('looping run')
		print('sleeping')
		time.sleep_ms(500)
		print('done')
		# run the robot and delay

	def calibrateend(self, x1, y1, x2, y2, a1, a2):
		#import math
		x_slip = x2-x1
		y_slip = y2-y1
		mean_a = (a1+a2)/2
		self.anglecalibration = math.degrees(math.atan2(y_slip, x_slip)) - mean_a
		# return the relevant angle
		# set this as the offset angle


	def runrobot(self):
		servolib.continuousservo.runallmotors()
		self.runtime = max([x.runtime for x in servolib.continuousservo._objs])

	def stoprobot(self):
		servolib.continuousservo.stopallmotors()