import RPi.GPIO as GPIO
from time import sleep,time
import sys
import curses

GPIO.setmode(GPIO.BOARD)


MOTOR_PIN=32

f=500

GPIO.setup(MOTOR_PIN,GPIO.OUT)

MOTOR_PWM=GPIO.PWM(MOTOR_PIN,f)

MOTOR_PWM.start(60)
print "init 0"
sleep(3)


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''

score = 60

try:
    while key != ord('q'):
        stdscr.refresh()
        print score
        key = stdscr.getch()
        #stdscr.addch(20,25,key)
        #stdscr.refresh()
        if key == curses.KEY_UP:
            score += 0.2
            MOTOR_PWM.ChangeDutyCycle(score)
        elif key == curses.KEY_DOWN:
            score -= 0.2
            MOTOR_PWM.ChangeDutyCycle(score)

finally:
    curses.endwin()
    MOTOR_PWM.stop()
    GPIO.cleanup()
