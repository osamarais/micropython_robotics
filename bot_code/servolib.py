#############################################################
# Library for continuous servo motor control with micropython
# ported to the ESP8266.
#
# Author: 	Osama Raisuddin
# 			METU Mechatronics
# ME462 Project
# Date of creation: 01-0.5-2018
#
##############################################################


import machine
import time

class continuousservo:

	"""A class for creating a continuous servo object

	Args:
		pin:		PWM signal pin connected to the servo. (Pin number, not Pin object)
					Must support PWM
		freq:		PWM frequency of servo.
					Standard: 	50 Hz for Analog Servos.
								300 Hz for Digital Servos
		minduty:	The lower limit on the duty cycle in microseconds.
		maxduty:	The upper limit on the duty cycle in microseconds.
						Note that the stopping duty cycle will be assumed to be
						the average of these two.


	Instance Properties:
		runtime:		The time for which we want the servo to move with
					the specified speed in ms.
		Speed:		The speed with which we want to move.
						Ranges from -100 to 100.

	Instance Methods:
		run():		This will check the remaining time and run the motor
					at the set speed.
	Class Methods:
		runallmotors():	This will do run() for all the continuous servo objects.




	Please note that this shall modify any previous configuration of the pin.
	On the ESP8266 the pins 0, 2, 4, 5, 12, 13, 14 and 15 all support PWM.


	"""


	_objs = []	# Registry to keep track of all continuousservo objects


	#def __init__(self, pin, freq = 50, minduty = 1000, maxduty = 1800, zerooffset = 5):
	def __init__(self, pin, freq = 50, minduty = 1200, maxduty = 1860, zerooffset = 5):

		self._pin = pin 			# Pin number
		self._freq = freq 			# PWM frequency
		self._minduty = minduty 	
		self._maxduty = maxduty 	
		self._duty = 0				# This is 0-1023 rather than in ms or us
		self._runtime = 0 			# The time in ms to run servo
		self._runinittime = 0 			# Time at which servo was started
		self._speed = 0 			# Servo speed
		self._isnewtime = False			# Whether or not a new run time was set
		self._zerooffset  = zerooffset


		# Make the Pin Object
		self._motorpin = machine.Pin(self._pin)
		# Make the PWM Object using the user's inputs, initialize at 0 velocity
		self._motorPWM = machine.PWM(self._motorpin, freq, int((self._maxduty+self._minduty)/2) )

		# Add to registry of continuousservo objects
		continuousservo._objs.append(self)



	# Make the freq a property
	@property
	def freq(self):
		return self._motorPWM.freq()
	# The method to set PWM freq
	@freq.setter
	def pin(self, newfreq):
		self._freq = newfreq
		self._motorPWM.freq(newfreq)


	# Make a property for the speed
	@property
	def speed(self):
		return self._speed
	# The method to set the new speed
	@speed.setter
	def speed(self, newspeed):
		zeroposition = (self._maxduty + self._minduty) / 2
		additionalposition = (self._maxduty - self._minduty) / 2 * newspeed / 100
		if additionalposition > 0:
			offset = self._zerooffset
		elif additionalposition < 0:
			offset = -self._zerooffset
		else:
			offset = 0
		conv = self._freq / 1000000 * 1024
		self._duty = int(conv*(zeroposition + additionalposition))+offset
		self._speed = newspeed
		self._isnewtime = True


	# Make a property for the runtime
	@property
	def runtime(self):
		return self._runtime
	# The method to set the new speed
	@runtime.setter
	def runtime(self, newruntime):
		self._runtime = newruntime
		self._isnewtime = True
		


	# This method will check the remaining time for the motor and start or stop it acordingly
	def run(self):
		if self._isnewtime:
			self._runinittime = time.ticks_ms()
			self._isnewtime = False

		remainingtime = time.ticks_diff(self._runinittime + self._runtime, time.ticks_ms())
		if remainingtime > 0:
			self._runtime = remainingtime
			self._runinittime = time.ticks_ms()
			self._motorPWM.duty(self._duty)
		else:
			self._runtime = 0
			self._motorPWM.duty(int((self._maxduty+self._minduty)/2))

	# This method will stop the motor and set the remaining time to zero
	def stop(self):
		self._runtime = 0
		self._isnewtime = True
		self._motorPWM.duty(int((self._maxduty+self._minduty)/2))


	# This class method will run the run() method for all motors
	# to easily start or stop them.
	@classmethod
	def runallmotors(cls):
		for obj in cls._objs:
			obj.run()
	
	# This class method will run the stop() method for all motors
	@classmethod
	def stopallmotors(cls):
		for obj in cls._objs:
			obj.stop()



	# This is the destructor method. It will deinitialize the PWM pin
	# and remove itself from the registry
	def __del__(self):
		# deinit the PWM pin
		self._motorPWM.deinit()
		# Remove from registry
		continuousservo._objs.remove(self)
		print('deleted continuousservo object')

