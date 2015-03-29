from threading import Thread
import time

class MyThread(Thread):
    def __init__(self):
        self.awake = False

    def run(self):
        time.sleep(5000)
        self.awake = True

    def is_sleeping(self):
        return not self.awake

class Main:
    
    def __init__(self):
        print "starting"
        self.blinked = False
        self.timer = MyThread()

    def state_machine(self, state):
        if self.blinked:
            state = 0
            return 0
        else:
            if self.timer.is_sleeping():
               return state
            else:
                state += 1
                self.start_timer()

    def start_timer(self):
        self.timer = MyThread.run() 

m = Main()
print m.state_machine(1)
