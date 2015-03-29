from osax import *
import time

sa = OSAX()

def mute_volume():
    sa.set_volume(0)

def restore_volume(volume):
    sa.set_volume(volume)
