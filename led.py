from gpiozero import LED
from time import sleep

led = LED(17)

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    led.close()
    print("GPIO cleanup completed") 