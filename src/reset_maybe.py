import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(12, 1000) # min throttle
pi.set_servo_pulsewidth(13, 1000) # min throttle
pi.set_servo_pulsewidth(18, 1000) # min throttle
pi.set_servo_pulsewidth(19, 1000) # min throttle
time.sleep(1)

pi.set_servo_pulsewidth(12, 2000) # max throttle
pi.set_servo_pulsewidth(13, 2000) # max throttle
pi.set_servo_pulsewidth(18, 2000) # max throttle
pi.set_servo_pulsewidth(19, 2000) # max throttle
time.sleep(1)

pi.set_servo_pulsewidth(12, 1500) # mean throttle
pi.set_servo_pulsewidth(13, 1500) # mean throttle
pi.set_servo_pulsewidth(18, 1500) # mean throttle
pi.set_servo_pulsewidth(19, 1500) # mean throttle

time.sleep(5)




pi.set_mode(12, pigpio.OUTPUT) # mot1
pi.write(12, 0)
pi.set_mode(13, pigpio.OUTPUT) # mot2
pi.write(13, 0)
pi.set_mode(18, pigpio.OUTPUT) # mot3
pi.write(18, 0)
pi.set_mode(19, pigpio.OUTPUT) # mot4
pi.write(19, 0)
