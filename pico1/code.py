# fightdeck - Pico 1
# Players 1 & 2 HID keyboard output
# https://github.com/LowPolyPhosphorus/fightdeck
#
# Requires CircuitPython + libraries:
#   adafruit_hid (copy to /lib/ on the Pico, from https://circuitpython.org/libraries unzip the file and find the folder named adafruit_hid)
#
# Wiring:
#   One pin -> GPIO, other pin -> GND for each button
#   Internal pull-ups enabled in software, so no external resistors needed

import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# (GPIO pin, Keycode)
# Order: P1 joystick diretions, P1 buttons, P2 joystick directions, P2 buttons

BUTTON_MAP = [ 
    # --- Player 1 ---
    (board.GP0, Keycode.UP_ARROW), # P1 Up
    (board.GP1, Keycode.DOWN_ARROW), # P1 Down
    (board.GP2, Keycode.LEFT_ARROW), # P1 Left
    (board.GP3, Keycode.RIGHT_ARROW), # P1 Right
    (board.GP4, Keycode.LEFT_CONTROL), # P1 Button 1 - Jump
    (board.GP5, Keycode.LEFT_ALT), # P1 Button 2 - Attack
    (board.GP6, Keycode.SPACE), # P1 Button 3 - Special

    # --- Player 2 ---
    (board.GP7, Keycode.R), # P2 Up
    (board.GP8, Keycode.F), # P2 Down
    (board.GP9, Keycode.D), # P2 Left
    (board.GP10, Keycode.G), # P2 Right
    (board.GP11, Keycode.A), # P2 Button 1 - Jump
    (board.GP12, Keycode.S), # P2 Button 2 - Attack
    (board.GP13, Keycode.Q), # P2 Button 3 - Special
]

# Set up buttons with internal pull-ups
buttons = []
for pin, _ in BUTTON_MAP:
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append(b)

# Track pressed state to avoid repeating key presses while held down
pressed = [False] * len(BUTTON_MAP)

while True:
    for i, (btn, (_, key)) in enumerate(zip(buttons, BUTTON_MAP)):
        is_pressed = not btn.value # active LOW: False = pressed

        if is_pressed and not pressed[i]:
            kbd.press(key)
            pressed[i] = True
        elif not is_pressed and pressed[i]:
            kbd.release(key)
            pressed[i] = False
    
    time.sleep(0.005) # 5ms polling = ~ 200Hz
