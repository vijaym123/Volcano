import time
from RPIO import PWM

generation=0
ENGINE_PIN=2
channel=2
#servo high is right turn
#servo low is left turn

def initchannel():
   global generation
   PWM.setup()
   PWM.init_channel(channel)
   print "init channel"
   generation=0
   
def initesc():
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1500)
   time.sleep(3)
   
def zapesc():
   brake = 150
   # move from 150 (brake) down three times then back to netural (brake)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1400)
   time.sleep(1)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1300)
   time.sleep(1)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1200)
   time.sleep(1)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, brake)
   
   #sleep for a while, then try forwards
   time.sleep(3)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1600)   
   time.sleep(1)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, brake)   
   #sleep a while
   time.sleep(3)
   #now backwards again then brake
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, 1300)   
   time.sleep(3)
   PWM.add_channel_pulse(channel, ENGINE_PIN, 0, brake)      
   time.sleep(3)
   
def cleanup():
   print "Cleaned up"
   PWM.cleanup()

initchannel()
initesc()

zapesc()

cleanup()

