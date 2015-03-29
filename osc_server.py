from liblo import *
from threading import Timer
from FSM import *

import sys
import time
import serial
import volume_control

class MuseServer(ServerThread):

    #listen for messages on port 5001
    def __init__(self):
        self.touching_forehead = False
        ServerThread.__init__(self, 5001)
        self.fsm = FSM()
        self.blink_count = 0;
        self.serialPort = serial.Serial('/dev/tty.usbmodem1411', 9600)
        time.sleep(2)
        self.write_to_port(10)
        self.prev = 0

    @make_method('/muse/elements/touching_forehead', 'i')
    def touching_forehead_callback(self, path, args):
        self.touching_forehead = args[0]

    @make_method('/muse/elements/blink', 'i') 
    def blink_callback(self, path, args):
        if not self.touching_forehead:
            return
        if not self.prev == self.fsm.state_machine():
            self.write_to_port(self.fsm.state_machine())
            self.manage_volume(self.prev, self.fsm.state_machine())
            print "state: {}".format(self.fsm.state_machine())
        self.prev = self.fsm.state_machine()
        self.fsm.update_blink(args[0])
        if args[0]:
            self.blink_count += 1
            print "blinked:{} times".format(self.blink_count) 

    def manage_volume(self, prev, cur_state):
        if cur_state == 4:
            volume_control.mute_volume()
        if cur_state == 0 and prev == 4:
            volume_control.restore_volume(2)

    def write_to_port(self, state):
        self.serialPort.write(str(state).encode())
        self.serialPort.flush()

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
   #start timing

if __name__ == "__main__":
    while 1:
        time.sleep(1)
