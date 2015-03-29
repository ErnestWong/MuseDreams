
#code snippet to communicate with mac serial port

import serial
import time

serialPort = serial.Serial('/dev/tty.usbmodem1411', 9600)
print "serial1"
time.sleep(1.5)
serialPort.write(str(1).encode())
print "serial2"
