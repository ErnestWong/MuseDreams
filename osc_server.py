from liblo import *
from threading import Timer
import sys
import time
from FSM import *

class MuseServer(ServerThread):

    #listen for messages on port 5001
    def __init__(self):
        self.touching_forehead = False
        ServerThread.__init__(self, 5001)
        self.fsm = FSM()
        self.blink_count = 0;

    @make_method('/muse/elements/touching_forehead', 'i')
    def touching_forehead_callback(self, path, args):
        self.touching_forehead = args[0]

    @make_method('/muse/elements/blink', 'i') 
    def blink_callback(self, path, args):
        print "state: {}".format(self.fsm.state_machine())
        self.fsm.update_blink(args[0])
        if args[0] and self.touching_forehead:
            self.blink_count += 1
            print "blinked:{} times".format(self.blink_count) 


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
