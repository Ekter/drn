import ftprci as fci
import time


acc = fci.sensor.LSM9DS1()

acc.check()

acc.full_settings()

while True:
    acc.read()
    print(acc.acceleration)
    time.sleep(1)

