import RPi.GPIO as GPIO
from time import sleep,time
import sys
import curses

GPIO.setmode(GPIO.BOARD)


ESC_PIN=32
SERVO_PIN=12
f=500

GPIO.setup(ESC_PIN,GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)


ESC_PWM=GPIO.PWM(ESC_PIN,f)
SERVO_PWM = GPIO.PWM(SERVO_PIN, 100)


ESC_PWM.start(60)
SERVO_PWM.start(5)
print "init"
sleep(3)


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''

accelerate = 60
turn = 15
try:
    while key != ord('q'):
        stdscr.refresh()
        print accelerate, turn
        key = stdscr.getch()
        #stdscr.addch(20,25,key)
        #stdscr.refresh()
        if key == curses.KEY_UP:
            accelerate += 0.2
            ESC_PWM.ChangeDutyCycle(accelerate)
        elif key == curses.KEY_DOWN:
            accelerate -= 0.2
            ESC_PWM.ChangeDutyCycle(accelerate)
        elif key == curses.KEY_RIGHT:
            turn -= 1
            SERVO_PWM.ChangeDutyCycle(turn)
            sleep(0.1)
            SERVO_PWM.ChangeDutyCycle(0)               
        elif key == curses.KEY_LEFT:
            turn += 1
            SERVO_PWM.ChangeDutyCycle(turn)
            sleep(0.1)
            SERVO_PWM.ChangeDutyCycle(0)  
finally:
    curses.endwin()
    ESC_PWM.stop()    
    SERVO_PWM.stop()
    GPIO.cleanup()
