
try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network

import esp
import claves

esp.osdebug(None)

import gc

gc.collect()

ssid = claves.name
claves = claves.passw

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, claves)

while station.isconnected() == False:
    pass

print("Connection successful")
print(station.ifconfig())

led = Pin(2, Pin.OUT)
led.on()

