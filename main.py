from threading import Timer
from FSM import *
from osc_server import *

import sys
import time
import serial
import volume_control


try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
