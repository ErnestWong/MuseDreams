from osax import *
import time

sa = OSAX()

def mute_volume():
    sa.set_volume(0)

def restore_volume(volume):
    sa.set_volume(volume)

def manage_volume(prev, cur_state):
    if cur_state == 4:
        mute_volume()
    if cur_state == 0 and prev == 4:
        restore_volume(5)


