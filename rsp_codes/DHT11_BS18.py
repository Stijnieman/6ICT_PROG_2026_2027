import time
import board
import adafruit_dht
from gpiozero import LED
from w1thermsensor import W1ThermSensor

red = LED(17)
yellow = LED(27)
green = LED(22)
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
volgnummer = 0

while True:
    try:
        temperature_in_celcius = sensor.get_temperature()
        temperature_c = dhtDevice.temperature    
        verschil = abs(temperature_c - temperature_in_celcius)

        green.off()
        yellow.off()
        red.off()

        if verschil < 1:
            green.on()
            color = "groene"
        elif verschil < 5:
            yellow.on()
            color = "gele"
        else:
            red.on()
            color = "rode"

        print(f"{volgnummer}: DHT11 = {temperature_c}, w1thermsensor = {temperature_in_celcius}, {color} LED gaat branden")
        volgnummer += 1

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

time.sleep(2.0)