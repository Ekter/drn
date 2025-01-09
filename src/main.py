import ftprci as fci
import time
import os

import pigpio

os.system("i2cdetect -y 1")

print("initializing LSM9DS1")
pi = pigpio.pi()
pi.set_mode(10, pigpio.OUTPUT) # GPIO 17 as output
pi.write(10, 1) # CS_AG
pi.set_mode(24, pigpio.OUTPUT) # GPIO 17 as output
pi.write(24, 0) # CS_M
pi.set_mode(11, pigpio.OUTPUT) # GPIO 17 as output
pi.write(11, 0) # SDO_AG
pi.set_mode(9, pigpio.OUTPUT) # GPIO 17 as output
pi.write(9, 0)  # SD0_M

os.system("i2cdetect -y 1")

acc = fci.sensor.LSM9DS1(1)
print("went ok")


time.sleep(1)
acc.check()

acc.full_settings()

while True:
    print(acc.read())
    pi.write(21, 1)
    pi.write(20, 0)
    time.sleep(0.5)
    pi.write(21, 0)
    pi.write(20, 1)
    pi.write(16,1)
    time.sleep(0.5)
    print(acc.read())
    pi.write(21, 1)
    pi.write(20, 0)
    time.sleep(0.5)
    pi.write(21, 0)
    pi.write(20, 1)
    pi.write(16,0)
    time.sleep(0.5)
