import RPi.GPIO as GPIO
from time import sleep,time
import sys

GPIO.setmode(GPIO.BOARD)
 

MOTOR_PIN=12

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
    while True:
       pulse_width = float(raw_input('pulse width ')) 
       MOTOR_PWM.ChangeDutyCycle(pulse_width)

finally :
  MOTOR_PWM.stop()
  GPIO.cleanup()
