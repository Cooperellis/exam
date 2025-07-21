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
while True:
    my_button.update()
    time.sleep(0.01)
    pause_time = knob.value/10000 + 1
    # Button release detected
    if my_button.rose:
        blue_led.value = False
        time.sleep(0.1)
        time.sleep(pause_time)
        blue_led.value = True
        timer = time.monotonic()
    if my_button.fell:
        reaction_time = timer
        print(f'{reaction_time}seconds!')

