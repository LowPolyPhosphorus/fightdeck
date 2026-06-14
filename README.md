# fightdeck
4 player TMNT arcade fight deck wired to two Raspberry Pi Picos acting as USB HID keyboards. Built for Fallout Fest as a hackathon project.

## what it does
- all 4 players output keyboard inputs via two Picos
- volume rocker works as media keys
- power switch puts the host machine to sleep
- works on Windows, Linux, RetroPie, and anything that accepts a USB keyboard

## hardware
- 2x Raspberry Pi Pico
- TMNT Arcade1Up 4 Player fight deck
- micro usb cables (optional a usb hub to make it only take up one cable and have a cleaner interface)
   
<sub> if you want to make this yourself, you can do it with just 2 players too!, just take the firmware from pico 1 or pico 2 if you have power and volume buttons (but you may have to remap the buttons) </sub>
| Item                   | Qty | Price  | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------|-----|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Raspberry Pi Pico 2Pcs | 1   | $14.59 | https://www.amazon.com/Raspberry-Pi-Pico-Development-Integrated/dp/B0BDLHMQ9C/ref=sr_1_1?crid=3HLWCUB48HJ6X&dib=eyJ2IjoiMSJ9.2DgeplSReQxI3NoQG6DUBY9gCzgNllj2yiY8xBkx7JMUW34yh80x4xR3CZBE6yy7_tfyFfoWvmv5LxD4Idl6edUHHHTypvZap_TRUiyagGDAPBkbTYhsvzghc44gBgz8nf_i8EKRk3WjwharvKg3JgiyaTJwb0WdTJA3mkxNaBacYhptYSXQ-wlJVcTdS_jWnH4rPa7dB2wt2VkpEqIX5YYyUi2vKhqHtteAGgnpBDA.aYwY7rWr27JXQH3ualWLxUriI3v4tz81XT691Xubr2g&dib_tag=se&keywords=raspberry+pi+pico&qid=1781469011&sprefix=raspberry+pi+pico%2Caps%2C207&sr=8-1 |


## pico layout 
- Pico 1: P1 + P2
- Pico 2: P3 + P4

## key mapping
standard MAME 4 player keyboard layout
| | Up | Down | Left | Right | Button 1 | Button 2 | Button 3 |
|-|----|----|----|----|----|----|-----|
| P1 | Up Arrow | Down Arrow | Left Arrow | Right Arrow | L-Ctrl | L-Alt | Space |
| P2 | R | F | D | G | A | S | Q |
| P3 | I | K | J | L | R-Shift | Enter | P |
| P4 | Num 8 | Num 2 | Num 4 | Num 6 | Num 0 | Num . | Num Enter |

## flashing 
1. hold BOOTSEL and plug in the pico
2. drag the CircuitPython UF2 onto RPI-RP2
3. copy the adafruit_hid folder into /lib/
4. drop boot.py and code.py onto the root of the device

## NES emulator tool
includes a browser based NES emulator page for demo purposes using EmulatorJS
 
1. put fightdeck-nes.html and your .nes ROM file in the same folder
2. open a terminal in that folder and run `python -m http.server 8080`
3. open `http://localhost:8080/fightdeck-nes.html` in your browser
4. type the ROM filename into the box and hit Launch
5. configure controls inside the emulator settings menu
note: you have to use the localhost URL, opening the HTML file directly will not work

## wiring
each button and joystick direction switch has two wires. one goes to a GPIO pin on the Pico, the other goes to ground. internal pull-ups are enabled in the firmware to prevent the need of resistors
all ground wires are bundled and soldered to a shared ground pin on each pico.
see `docs/pico1_pinout.csv` and `docs/pico2_pinout.csv` for the full pin assignment, and `docs/keymap.md` for the key mapping

## how to build it!
1. trace and label all the wires from the fight deck, one per button/direction
2. identify ground vs signal wire on each switch using a continuity tester (if you have an arduino you can test it with `tools/continuity_tester.ino`)
3. bundle wires by player group (P1+P2 for Pico 1, P3+P4+volume+power for Pico 2
4. solder all ground wires together and connect to a GND pin on the Pico
5. solder each signal wire to the GPIO pin listed in the pinout CSV
6. drag the .UF2 from [here](https://circuitpython.org/board/raspberry_pi_pico/) into the root of the folder, the pico will reboot and new files will appear, then download the bundle from [here](https://circuitpython.org/libraries), unzip it and find the folder labeled "adafruit_hid" and drag that into the /lib/ folder as per the flashing steps above
7. plug both picos into USB and test inputs in a text editor before launching anygame, then you can try launching .NES roms through the fightdeck-nes.html provided

## Why
I have had this fight deck for multiple years, and have attempted to make it to proper inputs before but never had done it as properly as I have this time, typically it was with random PC propiertary mapping as a joke or otherwise and not all of the buttons were wired since I only had an arduino. I have also for a long time, wanted to make a retropie/retroarch arcade cabinet and this brings me a step closer to ever doing that, plus this whole project was like 30 bucks with how cheap the fight deck was considering I found it at a Goodwill, purchasing a set of 12 buttons, and 4 joysticks would have easily exceeded that price. the buttons alone would probably be 30 bucks and it would be even more if you consider the materials for the entire enclosure.

## demo
see [here](https://youtu.be/bwVC0nnsRhk)

# Zine
<img alt="image" src="Zine/zine.png" />

# Gallery 
<img width="1194" height="885" alt="image" src="https://github.com/user-attachments/assets/8dc26584-57a8-4888-8b7b-ef3e8e566547" />
<img width="636" height="713" alt="image" src="https://github.com/user-attachments/assets/6fcce40b-f8c8-41ae-b160-0d901fd58d08" />
<img width="1180" height="885" alt="image" src="https://github.com/user-attachments/assets/77615d7d-591b-4753-8e99-85ea7a1da0e8" />
<img width="1180" height="885" alt="image" src="https://github.com/user-attachments/assets/185fb8f6-c311-47bb-8651-294e0cd51c1a" />
<img width="1873" height="856" alt="image" src="https://github.com/user-attachments/assets/794940f0-1ec1-4be2-a752-e49a8b91a7d7" />
> Some of these photos are older and were taken before it was finished, the final build has the picos fully soldered
