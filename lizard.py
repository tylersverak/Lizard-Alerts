#NOTE: will NOT work overnight due to handling of hours
# from imageupload import *
# from takepicture import *
from smshandler import *
from gpiozero import DistanceSensor
from datetime import datetime
import time
import requests


CURRENT_NGROK = 'https://e7b4fa384181.ngrok.io' # ngrok url changes every time a tunnel is opened

# given a list of ints representing the time in hours, minutes, seconds, and past values for hours and minutes,
# returns True if five minutes have passed otherwise returns False
def five_after(hms, h, m):
  min_wait = 5
  if h == hms[0]:
    return m + min_wait <= hms[1]
  return 60 - m + hms[1] >= min_wait
  

def run():
    ultrasonic = DistanceSensor(echo=17, trigger = 4)
    ultrasonic.threshold_distance = .5 #distance in meters
    ultrasonic.max_distance = 2
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hms = current_time.split(':')
    hms = [int(i) for i in hms]
    hours = hms[0]
    minutes = hms[1] - 5
    while True:
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      hms = current_time.split(':')
      hms = [int(i) for i in hms]
      if (ultrasonic.distance < 0.28 and five_after(hms, hours, minutes)): # if it's been more than 5 minutes and the lizard is in the middle of the cage
        filename = 'tracy_' + str(hms[0]) + ':' + str(hms[1])
        #take_picture('lizardpictures/', filename)
        send_text(CURRENT_NGROK)#192.168.4.45:8000/lizardpictures/' + filename + '.jpg')
        print('Snap!')
        hours = hms[0]
        minutes = hms[1]
      time.sleep(3)
      if (hms[2] < 6 and hms[1] < 2):
        print('top of hour ' + str(hms[0]))

if __name__ == "__main__":
    run()