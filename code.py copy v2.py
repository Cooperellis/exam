import digitalio
import board
import time
from adafruit_debouncer import Debouncer
import analogio
# Setup button and LEDs
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
my_button = Debouncer(button)

blue_led = digitalio.DigitalInOut(board.GP16)
blue_led.direction = digitalio.Direction.OUTPUT

knob = analogio.AnalogIn(board.A0)
blue_led.value = True
reaction_time = 0
attempt = False
reaction_time = 0
while True:
    my_button.update()
    pause_time = knob.value/10000 + 1
    time.sleep(0.001)
    if my_button.rose:  # Button release detected
        blue_led.value = False
        time.sleep(pause_time)  # Pauses for how long the knob is set to
        blue_led.value = True  # Blue LED on
        attempt = True

    reaction_time += 1

    if my_button.fell:  # Button press detected
        if attempt is True:
            print(f"Your reaction time was {reaction_time} ms!")
            reaction_time = 0
            blue_led.value = False
            break
