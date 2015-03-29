
#code snippet to communicate with mac serial port

import serial
serialPort = serial.Serial('/dev/cu.usbmodem1421', 9600)
serialPort.write(str(1).encode())
print(serialPort.readline()) 