import RPIO.PWM as PWM
import time
GPIO = 3
CHANNEL = 3

PWM.set_loglevel(PWM.LOG_LEVEL_DEBUG)

PWM.setup()
PWM.init_channel(CHANNEL)
PWM.print_channel(CHANNEL)

PWM.add_channel_pulse(CHANNEL, GPIO, 0, 50)
time.sleep(2)
PWM.add_channel_pulse(CHANNEL, GPIO, 100, 50)
