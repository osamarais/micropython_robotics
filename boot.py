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

wlan = network.WLAN(network.STA_IF)