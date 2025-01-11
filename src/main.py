import ftprci as fci
import time
import os

import pigpio

os.system("i2cdetect -y 1")

print("initializing LSM9DS1")
pi = pigpio.pi()

pi.set_mode(10, pigpio.OUTPUT)  # CS_AG
pi.write(10, 1)
pi.set_mode(24, pigpio.OUTPUT)  # CS_M
pi.write(24, 1)
pi.set_mode(11, pigpio.OUTPUT)  # SDO_AG
pi.write(11, 0)
pi.set_mode(9, pigpio.OUTPUT)   # SD0_M
pi.write(9, 0)

pi.set_mode(16, pigpio.OUTPUT) # leds
pi.write(16, 0)
pi.set_mode(20, pigpio.OUTPUT)
pi.write(20, 0)
pi.set_mode(21, pigpio.OUTPUT)
pi.write(21, 0)

pi.set_mode(12, pigpio.OUTPUT) # mot1
pi.write(12, 0)
pi.set_mode(13, pigpio.OUTPUT) # mot2
pi.write(13, 0)
pi.set_mode(18, pigpio.OUTPUT) # mot3
pi.write(18, 0)
pi.set_mode(19, pigpio.OUTPUT) # mot4
pi.write(19, 0)


# http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
# http://abyz.me.uk/rpi/pigpio/python.html#set_PWM_range

os.system("i2cdetect -y 1")

acc = fci.sensor.LSM9DS1()
print("went ok")


time.sleep(1)
acc.check()

acc.full_settings()
print(f"reg CTRL_REG1_G state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG1_G, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG2_G state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG2_G, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG3_G state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG3_G, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG4 state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG4, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG5_XL state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG5_XL, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG6_XL state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG6_XL, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG7_XL state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG7_XL, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG8 state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG8, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG9 state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG9, max_bytes=1)[0]:08b}")
print(f"reg CTRL_REG10 state:{acc.accgyro.read(address=acc.RegsAccGyro.CTRL_REG10, max_bytes=1)[0]:08b}")

while True:
    print(acc.read())
    pi.write(21, 1)
    pi.write(20, 0)
    pi.write(16,0)
    time.sleep(1/3)
    pi.write(21, 0)
    pi.write(20, 1)
    pi.write(16,0)
    time.sleep(1/3)
    pi.write(21, 0)
    pi.write(20, 0)
    pi.write(16,1)
    time.sleep(1/3)
