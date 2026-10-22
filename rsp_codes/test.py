from gpiozero import LED, MCP3008
from time import sleep

led = LED(26)

while True:
    pot = MCP3008(0)
    led.on()
    sleep(pot.value)
    led.off()
    sleep(pot.value)