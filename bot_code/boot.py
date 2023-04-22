# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

# This part is added by me
import os
import network
import machine
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ME46x','mechastudent')

#from robotlib import *
#r = robot()
#
#from socketlib import *
#sock = UDP(wlan,8001)
#
#from ledpwm import *
#
#from program import *
exec(open('robotlib.py').read())
exec(open('socketlib.py').read())
exec(open('ledpwm.py').read())
exec(open('program.py').read())
exec(open('PID.py').read())
exec(open('newfollower.py').read())
exec(open('predatorprey.py').read())


sock = UDP(wlan,8001)
r = robot()
#parsedata(sock)

mypid = PID(1,0,0)
