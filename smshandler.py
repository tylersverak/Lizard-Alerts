# Tyler Sverak 12-23-2020
# some variable values have been replaced for privacy reasons
import requests
import os
from twilio.rest import Client
import random

# using ngrok, if you end up using it- start by finding ngrok application, when prompt opens type ./ngrok http 127.0.0.1:5000 and to kill it type taskkill /f /im ngrok.exe

tracy_quips = ['Look how cute Tracy is!', 'Woah, Tracy, looking good!', "Look who's out from under his rock!", 'Happy Holidays, from Tracy.', 'Tracy sure is active today!',
                "Me: :) Tracy:^v^ Me: :)))))", "The lizard is on the move", 'Tracy is soaking up some sun! Or rather, soaking up some... lamp?', 'Bugs beware, lizard on the loose!']
phones =['+19255968020']

# given a url, sends that url and a fun quip to all the numbers in phones
def send_text(imageurl):
  account_sid = # *sid goes here*
  auth_token = # *auth token goes here*
  client = Client(account_sid, auth_token)
  stuff = tracy_quips[random.randint(0, len(tracy_quips) - 1)]
  print(stuff)
  for number in phones:
    message = client.messages \
        .create(
             body=stuff + '\n' + imageurl,
             from_='+17192662672',
             to=number
         )
  print(message.sid)

if __name__ == "__main__":
    send_text('https://*ip address*:8000/lizardpictures/')
