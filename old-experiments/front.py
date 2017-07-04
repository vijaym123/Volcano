import RPi.GPIO as GPIO
from time import sleep,time
import sys

GPIO.setmode(GPIO.BOARD)
 

MOTOR_PIN=3

f=500

GPIO.setup(MOTOR_PIN,GPIO.OUT)

MOTOR_PWM=GPIO.PWM(MOTOR_PIN,f)

MOTOR_PWM.start(60)
print "init 0"
sleep(3)
try :
    while True:
       pulse_width = float(raw_input('pulse width '))
       MOTOR_PWM.ChangeDutyCycle(pulse_width)
       sleep(0.2)

finally :
  MOTOR_PWM.stop()
  GPIO.cleanup()
