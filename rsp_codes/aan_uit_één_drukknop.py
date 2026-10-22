from gpiozero import Button, LED
from signal import pause

button = Button(26)
led = LED(2)

button.when_pressed = led.toggle
pause()