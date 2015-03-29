from threading import Timer
import time

class Main:

    def __init__(self):
        print "starting"
        self.blinked = False
        self.timing = False
        self.state = 0

    def state_machine(self):
        if self.blinked:
            self.state = 0
            return self.state
        else:
            if self.timing:
                print 'return state'
                return self.state
            else:
                self.start_timer()
                self.state += 1
                return self.state

    def start_timer(self):
        print "starting timer"
        self.timing = True
        t = Timer(5, self.stop).start()

    def stop(self):
        print "stopped"
        self.timing = False

m = Main()
while True:
    time.sleep(1)
    print m.state_machine()
