import RPi.GPIO as GPIO
from time import sleep,time
import sys

GPIO.setmode(GPIO.BOARD)


MOTOR_PIN=32

frequency=50

def getDutyCycle(pulse_width, frequency):
    time_period=1000.0/frequency
    duty_cycle=pulse_width*100.0/time_period
    return duty_cycle

GPIO.setup(MOTOR_PIN,GPIO.OUT)

MOTOR_PWM=GPIO.PWM(MOTOR_PIN,frequency)

MOTOR_PWM.start(getDutyCycle(1.5, frequency))
sleep(3)

try :
    input_commands = {"forward": 1.56, "set_back" : 1.3, "break" : 1.5, "reverse": 1.4}
    while True:
       pulse_width = input_commands['forward']
       while pulse_width<=1.58:
           MOTOR_PWM.ChangeDutyCycle(getDutyCycle(pulse_width, frequency))
           print "Going Foward with : ", pulse_width
           sleep(5)
           pulse_width+=0.01

       pulse_width = input_commands['set_back']
       MOTOR_PWM.ChangeDutyCycle(getDutyCycle(pulse_width, frequency))
       print "Setting back with : ", pulse_width
       sleep(2)

       pulse_width = input_commands['break']
       MOTOR_PWM.ChangeDutyCycle(getDutyCycle(pulse_width, frequency))
       print "Setting break with : ", pulse_width
       sleep(2)

       pulse_width = input_commands['reverse']
       while pulse_width>=1.3:
           MOTOR_PWM.ChangeDutyCycle(getDutyCycle(pulse_width, frequency))
           sleep(5)
           print "Going back with : ", pulse_width
           pulse_width-=0.01

finally :
  MOTOR_PWM.stop()
  GPIO.cleanup()
