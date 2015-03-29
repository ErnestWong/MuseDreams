
#code snippet to communicate with mac serial port

import serial
serialPort = serial.Serial('/dev/tty.usbmodem1411', 9600)
serialPort.write(str(1).encode())
print(serialPort.readline())
