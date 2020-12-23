# Lizard-Alerts
setting up text alerts to a live video feed for when the lizard moves

Requirements to Run- ngrok, running ngrok tunnel to localhost, import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

Summary- 

Shortcomings and Possible Improvements My first issue was how to get the fields I needed from the beautifulsoup object, which contained the HTML. My stradegies involved trying to gather the information back into a json file and writing my own grammar to create a data structure with the data I needed, but these failed because I could not find where the json file began and ended and there were too many unique cases for my own grammar to work. Another solution I discovered after was using a regex, and while this might be the best tool for the job, I am not currently comfortable enough with it to use it in this project. Instead, I created a list of my desired fields and searched for them in large strings that were in the HTML tags. This process taught me a lot about tackling large scale, difficult problems and the BeautifulSoup library. Next was graphing the data, which required me to remember and learn a ton of new tools in seaborn, pandas, and matplotlib. Because of the difference of sizes and prestige to each tournament, it was difficult to find a numerical way to rank them. I didn't want to ignore certain outlier results, but including them in the graph scale made it harder to intrepret the data. If I were to improve this project, I would include more graphs that would show zoomed in versions of previous graphs that were more difficult to understand. The information I got was just from the results page, but I also figured out I could use the urls found in the results page to go to the results page of each specific tournament and find a ton more data. I didn't want to do this with this project because I felt the amount of data was unnecessary and it would involving scraping hundreds of web pages which would drastically increase runtime. This might be a cool addition in the future if I can come up with creative ways to display the new information. Lastly, the color scheme isn't perfect, and while I personally love the yellow/black/rainbow color scheme, I think adapting the color of some parts of the graph would make it more appealing to a wider audience.
