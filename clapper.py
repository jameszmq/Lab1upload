import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
SPI_PORT=0
SPI_DEVICE=0
mcp=Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
last=100
flag=0
def checkEnv():
    global last
    newval = mcp.read_adc(2)
    if newval - last > 60:
        global flag
        if  flag==0:
            GPIO.output(22, GPIO.HIGH)
            flag=1
        else:
            GPIO.output(22, GPIO.LOW)
            flag=0
    last = newval
print("Ctrl+C to exit")
while 1==1:
    try:
        checkEnv()
        time.sleep(0.01)
    except KeyboardInterrupt:
        exit(0)
