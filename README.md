# Lizard-Alerts
setting up text alerts to a live video feed for when the lizard moves

Requirements to Run- ngrok, running ngrok tunnel to localhost, picamera, http, gpiozero, requests, twilio library and account
ngrok is a service that allows you to show your localhost on a real shareable url, picamera is the library for raspberry pi involved with the camera, gpiozero has python functions that make it easier to use the distance sensor, twilio is an api and service that allows you to automate sms messages.

Summary- My friend was going away for the week and wanted me to watch her lizard. I noticed that the lizard (Tracy) was usually content in staying in one of his two caves and didn't come out often. I wanted a fun way of knowing when he was out of his cave and wanting a text of him on the move every time it happened. First, I set up a distance sensor pointed at the intersection where the lizard crosses between the two caves. From the top to the bottom of the tank was roughly 29 centimeters, so I set it such that when the distance is less than 28 it would mean the lizard must be there. Because the lizard is slow, I used sleep() to have it check once every three seconds or so. I also used datetime objects to make sure that if he parked himself in the middle of his tank, it would wait 5 minutes before sending another notification. Next I set up my picamera to take a picture of him and store it whenever he tripped the distance sensor. Next issue was sending a text with my trial Twilio account. Normally you can send images by including them in the "media" parameter when sending a texts, but when using a simplehttp (python library for setting up basic http server) server the texts didn't go through. The link worked in my browser on a seperate machine, and image links to pictures I found on Google worked, so I imagined for some reason Twilio services didn't like the simplehttp url. I ended up changning my approach so instead of taking a picture, I would use code from the picamera documentation to stream video of the inside of the tank on localhost and then use ngrok to provide a tunnel from localhost to a real url. Because my ngrok account is also not premium, the url changes each time I open the tunnel. I then save the generated url into lizard.py so it can pass the website name as a parameter to smshandler, which includes the link in the body of the text with a fun quip. It then texts me the message. I didn't want to pay for the extra features of these services because Tracy is only here for a week and I would have a hard time making use of these services after.

I forgot I left the program running while on a zoom call with friends, but was elated when I realized what the text messaged I received was. In my excitement I forgot to take a decent screenshot but in the one I provide you can still see the end of Tracy's tail. I also send the livestream link to my friend so she could check in on Tracy when she wanted to.

Shortcomings and Possible Improvements- several shortcomings and limitations of the project would be solved by paying, like a permanent ngrok link. Additionally, I would've liked to figure out how to get Twilio to send a picture from my server so it would display without having to click on the link, and with pictures you don't have to go to the livestream immediately after receiving the text to see Tracy. Currently, keeping the program running requires my desktop to be on and communicating with my raspberry pi via SSH. By using Linux tools or by setting the pi up with a monitor, I could have it run on its own, but Tracy is only here for so long and my computer is usually on anyway. Having the camera angle change to follow Tracy is another possible improvement. I was able to set up my own http server to display each image when its taken, and if I could figure out a way to send that link without Twilio would also be a big step up. If this were the case, I would have to wait until Tracy is directly in front of the camera for the best possible shot. Using a background substraction algorithm with opencv would be great for a job like that.

Directions- open ngrok tunnel to localhost 8000, then copy url generated and put it as the CURRENT_NGROK variable in lizard.py. Run rpi.py then lizaard.py.
