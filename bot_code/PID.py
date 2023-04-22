import time

class PID():
	def __init__(self, P = 1,I = 0, D = 0):
		self.P = P
		self.I = I
		self.D = D

		self.__lasttime = time.ticks_ms()
		self.__currenttime = time.ticks_ms()

		self.__Pterm = 0
		self.__Iterm = 0
		self.__Dterm = 0
		self.__lasterror = 0

		self.windup = 10

		self.saturation = 100

	def controlcommand(self,error):

		self.__currenttime = time.ticks_ms()
		delta_time = time.ticks_diff(self.__currenttime, self.__lasttime) * 1000
		delta_error = error - self.__lasterror

		if (delta_time > 0):
			self.__Pterm = error
			self.__Iterm = self.__Iterm + (error + self.__lasterror)/2 * delta_time
			self.__Dterm = delta_error / delta_time

			if (self.__Iterm > self.windup):
				self.__Iterm = self.windup
			elif (self.__Iterm < -self.windup):
				self.__Iterm = -self.windup

			output = self.P * self.__Pterm + self.I * self.__Iterm + self.D * self.__Dterm

			if output > self.saturation:
				output = self.saturation
			elif output < -self.saturation:
				output = -self.saturation
			
		else:
			output = 0


		self.__lasttime = self.__currenttime
		self.__lasterror = error

		return output

		








