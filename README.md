## Button Library for Raspberry Pi Pico - DIYables_Pico_Button
This MicroPython library is designed for Raspberry Pi Pico to make it easy to use push button, momentary switches, toggle switch, magnetic contact switch (door sensor)... It is easy to use for not only beginners but also experienced users... 

It is created by DIYables to work with DIYables products, but also work with products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.



Features
----------------------------
* Works with any Raspberry Pi Pico board.
* Supports the internal pull-up/pull-down resistor to avoid the floating value
* Supports debounce to eliminate the chattering phenomenon
* Supports the pressed and released events
* Supports the counting (for FALLING, RISING and BOTH)
* Easy to use with multiple buttons
* All functions are non-blocking 


Available Functions
----------------------------
* __init__(pin, mode=Pin.PULL_UP)
* set_debounce_time(time_ms)
* get_state()
* get_state_raw()
* is_pressed()
* is_released()
* set_count_mode(mode)
* get_count()
* reset_count()
* loop()


Available Examples
----------------------------
* pull_up.py
* pull_down.py



Tutorials
----------------------------
* [Raspberry Pi Pico - Button](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-button)
* [Raspberry Pi Pico - Button Debounce](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-button-debounce)


References
----------------------------
* [Raspberry Pi Pico - Button Library](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-button-library)
