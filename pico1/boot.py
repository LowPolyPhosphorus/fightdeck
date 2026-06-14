# fightdeck - Pico 1
# boot.py - enables USB HID before CircuitPython starts main code.py
# https://github.com/LowPolyPhosphorus/fightdeck
#
# This file runs once at boot, before code.py
# Drop this on the root of the Pico alongside code.py

import usb_hid
usb_hid.enable((usb_hid.Device.KEYBOARD,))