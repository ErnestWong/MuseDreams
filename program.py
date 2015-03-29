from threading import Timer
import time

class Main:
    
    def __init__(self):
        print "starting"
        self.blinked = False
        self.timing = False
        self.state = 0

    def state_machine(self, state):
        if self.blinked:
            self.state = 0
            return self.state
        else:
            if self.timing:
                print 'return state'
                return state
            else:
                self.start_timer()
                return state + 1

    def start_timer(self):
        print "starting timer"
        self.timing = True
        t = Timer(5, self.stop)

    def stop(self):
        print "stopped"
        self.timing = False

m = Main()
print m.state_machine(1)
time.sleep(3)
print m.state_machine(1)
