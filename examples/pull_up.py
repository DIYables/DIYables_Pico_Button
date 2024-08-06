"""
Wiring instructions when using PULL_UP:
- Connect one terminal of the button to GPIO 14 on the Raspberry Pi Pico.
- Connect the other terminal of the button to the ground (GND).
# The GPIO pin is set to use an internal pull-up resistor.
"""

from DIYables_Pico_Button import DIYables_Pico_Button
import time

button = DIYables_Pico_Button(14)  # Pin number 14, for example, PULL_UP is default
button.set_debounce_time(50)  # Set debounce time to 50 milliseconds

while True:
    button.loop()
    if button.is_pressed():
        print("Button Pressed")
    if button.is_released():
        print("Button Released")
    time.sleep(0.01)  # Small delay to be gentle on the CPU

