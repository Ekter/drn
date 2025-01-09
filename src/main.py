import ftprci as fci
import time

import pigpio

print("initializing LSM9DS1")
acc = fci.sensor.LSM9DS1(1)
print("went ok")

led1 = pigpio.LED(21)

led1.on()
time.sleep(1)
led1.off()
acc.check()

acc.full_settings()

while True:
    acc.read()
    print(acc.acceleration)
    time.sleep(1)

