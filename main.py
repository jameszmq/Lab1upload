import time
import datetime
import numpy as np
import matplotlib as plot
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

Temp_arr = np.zeros(60)
Hum_arr = np.zeros(60)
Light_arr = np.zeros(60)
Gate_arr = np.zeros(60)
Envelop_arr = np.zeros(60)
Audio_arr = np.zeros(60)

for x in range(60):

    print("Time = " + datetime.datetime.now().strftime('%H:%M:%S'))
    hum, temp = Adafruit_DHT.read_retry(22, 4)
    if hum is not None and temp is not None:
        print('Temp = {0:0.1f}\nHum = {1:0.1f}%'.format(temp, hum))
    else:
        print("Failed to grab temp and hum data.")
    light = mcp.read_adc(3)
    print("Light = " + str(light))
    gate = mcp.read_adc(2)
    if gate > 1000:
        Gate_arr[x]=1
        print("Gate = 1")
    else:
        Gate_arr[x]=0
        print("Gate = 0")
    envelop = mcp.read_adc(1)
    print("Envelop = " + str(envelop))
    audio = mcp.read_adc(0)
    print("Audio = " + str(audio) + '\n')
    Temp_arr[x]=temp
    Hum_arr[x]=hum
    Light_arr[x]=light
    Envelop_arr[x]=envelop
    Audio_arr[x]=audio
    time.sleep(60)

np.save("Temp_data", Temp_arr)
np.save("Hum_data", Hum_arr)
np.save("Light_data", Light_arr)
np.save("Gate_data", Gate_arr)
np.save("Envelop_data", Envelop_arr)
np.save("Audio_data", Audio_arr)
