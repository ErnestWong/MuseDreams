from threading import Timer
import time

class FSM():

    def __init__(self):
        print "starting"
        self.blinked = False
        self.timing = False
        self.error = False
        self.state = 0

    def update_blink(self, blink):
        self.blinked = blink

    def update_error(self, forehead):
        self.error = forehead

    def state_machine(self):
        if self.blinked:
            self.state = 0
            return self.state
        else:
            if self.state == 4:
                return self.state
            if self.timing:
                return self.state
            else:
                self.start_timer()
                self.state += 1
                return self.state

    def start_timer(self):
        self.timing = True
        t = Timer(3, self.stop).start()

    def stop(self):
        self.timing = False
