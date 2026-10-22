# import adafruit_dht
# from gpiozero import MCP3008
# from time import sleepimport board 

# dhtDevice = adafruit_dht.DHT11(board.D18)
# adc = MCP3008(channel=0)
# f = open("mijndata.csv","w")
# volgnummer = 0
# while True:
#     try:
#         volgnummer += 1

#         temp_dht = dhtDevice.temperature
#         temp_tmp = (adc.value * 5 - 0.5) * 100

#         gem = (temp_dht + temp_tmp) / 2
#         ver = abs(temp_dht - temp_tmp)

#         f.write(f"{volgnummer},{temp_dht},{temp_tmp},{ver},{gem}")
#     except RuntimeError as error:
#         print(f"Fout bij uitlezen sensor: {error}")
#     except Exception as error:
#         print(f"Onverwachte fout: {error}")
#         break
#     sleep(3)