import ftprci as fci
import time

import pigpio

print("initializing LSM9DS1")
acc = fci.sensor.LSM9DS1(1)
print("went ok")

pi = pigpio.pi()

time.sleep(1)
acc.check()

acc.full_settings()

while True:
    print(acc.read())
    pi.write(21, 1)
    time.sleep(0.5)
    pi.write(21, 0)
    time.sleep(0.5)
