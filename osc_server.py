from liblo import *
import sys
import time

class MuseServer(ServerThread):

    #listen for messages on port 5001
    def __init__(self):
        self.touching_forehead = False
        ServerThread.__init__(self, 5001)
        self.blink_count = 0;
        self.blinked = false;

    @make_method('/muse/elements/touching_forehead', 'i')
    def touching_forehead_callback(self, path, args):
        self.touching_forehead = args[0]

    @make_method('/muse/elements/blink', 'i') 
    def blink_callback(self, path, args):
        self.blinked = args[0]
        if blinked and self.touching_forehead:
            self.blink_count += 1
            print "blinked: {}, {} times".format(blinked,self.blink_count) 


try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
while not server.blinked
    #start timing

if __name__ == "__main__":
    while 1:
        time.sleep(1)
