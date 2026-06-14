import board, digitalio, usb_hid, time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

BUTTON_MAP = [
    # --- Player 3 ---
    (board.GP0, Keycode.I),           # P3 Up
    (board.GP1, Keycode.K),           # P3 Down
    (board.GP2, Keycode.J),           # P3 Left
    (board.GP3, Keycode.L),           # P3 Right
    (board.GP4, Keycode.RIGHT_SHIFT), # P3 Button 1 - Jump
    (board.GP5, Keycode.RETURN),      # P3 Button 2 - Attack
    (board.GP6, Keycode.P),           # P3 Button 3 - Special

    # --- Player 4 ---
    (board.GP7,  Keycode.KEYPAD_EIGHT),  # P4 Up
    (board.GP8,  Keycode.KEYPAD_TWO),    # P4 Down
    (board.GP9,  Keycode.KEYPAD_FOUR),   # P4 Left
    (board.GP10, Keycode.KEYPAD_SIX),    # P4 Right
    (board.GP11, Keycode.KEYPAD_ZERO),   # P4 Button 1 - Jump
    (board.GP12, Keycode.KEYPAD_PERIOD), # P4 Button 2 - Attack
    (board.GP13, Keycode.KEYPAD_ENTER),  # P4 Button 3 - Special
]

# Volume rocker pins
vol_up_pin = digitalio.DigitalInOut(board.GP14)
vol_up_pin.direction = digitalio.Direction.INPUT
vol_up_pin.pull = digitalio.Pull.UP

vol_down_pin = digitalio.DigitalInOut(board.GP15)
vol_down_pin.direction = digitalio.Direction.INPUT
vol_down_pin.pull = digitalio.Pull.UP

# Power/sleep switch (latching)
power_pin = digitalio.DigitalInOut(board.GP16)
power_pin.direction = digitalio.Direction.INPUT
power_pin.pull = digitalio.Pull.UP

buttons = []
for pin, _ in BUTTON_MAP:
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append(b)

pressed = [False] * len(BUTTON_MAP)
last_power_state = not power_pin.value  # invert so first flip always triggers

while True:
    # Regular buttons
    for i in range(len(BUTTON_MAP)):
        is_pressed = not buttons[i].value
        key = BUTTON_MAP[i][1]
        if is_pressed and not pressed[i]:
            kbd.press(key)
            pressed[i] = True
        elif not is_pressed and pressed[i]:
            kbd.release(key)
            pressed[i] = False

    # Volume rocker
    if not vol_up_pin.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
    if not vol_down_pin.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)

    # Power switch (latching)
    # OFF transition -> Windows sleep shortcut (Win+X, U, S)
    # ON transition -> harmless keypress to wake PC via HID activity
    current_power = power_pin.value
    if current_power != last_power_state:
        if current_power:  # switched to OFF - sleep
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.X)
            kbd.release(Keycode.X)
            kbd.release(Keycode.WINDOWS)
            time.sleep(0.5)
            kbd.press(Keycode.U)
            kbd.release(Keycode.U)
            time.sleep(0.3)
            kbd.press(Keycode.S)
            kbd.release(Keycode.S)
        else:  # switched to ON - wake
            kbd.press(Keycode.RIGHT_SHIFT)
            time.sleep(0.05)
            kbd.release(Keycode.RIGHT_SHIFT)
        last_power_state = current_power

    time.sleep(0.005)