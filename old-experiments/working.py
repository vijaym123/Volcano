import RPi.GPIO as GPIO
from time import sleep,time
import sys

GPIO.setmode(GPIO.BOARD)


MOTOR_PIN=32

f=500

GPIO.setup(MOTOR_PIN,GPIO.OUT)

MOTOR_PWM=GPIO.PWM(MOTOR_PIN,f)

MOTOR_PWM.start(60)
print "init 0"
sleep(3)
try :
    while True:
       i=65
       while i<=70:
          print "FORWARD : ", i
          MOTOR_PWM.ChangeDutyCycle(i)
          sleep(0.2)
          i+=0.1

       i=58
       while i>=55:
          print "BREAK : ", i
          MOTOR_PWM.ChangeDutyCycle(i)
          sleep(0.01)
          i-=0.1

       i=0
       while i<=5:
          print "RUN BACKWARD : ", i
          MOTOR_PWM.ChangeDutyCycle(i)
          sleep(0.2)
          i+=0.01

       i=58
       while i>=55:
          print "SET BREAK : ", i
          MOTOR_PWM.ChangeDutyCycle(i)
          sleep(0.2)
          i-=0.1

finally :
  MOTOR_PWM.stop()
  GPIO.cleanup()
