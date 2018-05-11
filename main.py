# some stuff added for our robot

import time

from robotlib import *
r = robot()

speed = 15
size = 1000
dtime = 500
stime = 10
# make a square with the robot
r.translate(speed,size,0)
while r._front._runtime > 0:
	r.runrobot()
	time.sleep_ms(stime)
r.runrobot()
time.sleep_ms(dtime)

r.translate(speed,size,90)
while r._front._runtime > 0:
	r.runrobot()
	time.sleep_ms(stime)
r.runrobot()
time.sleep_ms(dtime)

r.translate(speed,size,180)
while r._front._runtime > 0:
	r.runrobot()
	time.sleep_ms(stime)
r.runrobot()
time.sleep_ms(dtime)

r.translate(speed,size,270)
while r._front._runtime > 0:
	r.runrobot()
	time.sleep_ms(stime)
r.runrobot()
time.sleep_ms(dtime)
r.runrobot()
