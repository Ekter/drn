import pigpio

pi = pigpio.pi()


pi.set_mode(12, pigpio.OUTPUT) # mot1
pi.write(12, 0)
pi.set_mode(13, pigpio.OUTPUT) # mot2
pi.write(13, 0)
pi.set_mode(18, pigpio.OUTPUT) # mot3
pi.write(18, 0)
pi.set_mode(19, pigpio.OUTPUT) # mot4
pi.write(19, 0)
