#!/usr/bin/env python
# -*- coding: utf-8 -*-


fontLight = 'Lato Light', 22, 'normal'
fontBold = 'Lato Light', 80, 'normal'
background = '#000000'
frontground = '#FFFFFF'


from Tkinter import *
import time

currentTime = int(time.strftime('%H:%M').split(':')[0])  
if currentTime < 12 :
     welcome = 'Good morning'
if currentTime > 12 and currentTime < 18  :
     welcome = 'Good afternoon'
if currentTime > 18 :
     welcome = 'Good evening'
 


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()


song = Label(root, font=(fontLight),text=welcome, bg=background, fg=frontground)
song.pack(fill=BOTH, expand=1)
song.place(y = (h*0.95))

root.attributes("-fullscreen", True)
root.configure(background=background)
time1 = ''
clock = Label(root, font=(fontBold), bg=background, fg=frontground)
clock.pack(fill=BOTH, expand=1)
clock.place(x = 0, y = 0)

def tick():
    global time1 
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


import urllib2
import json
req = urllib2.Request("https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%2C%20location.city%20from%20weather.forecast%20where%20woeid%20%3D%2012818409&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())

city = Label(root, font=(fontLight),text=json['query']['results']['channel']['location']['city'], bg=background, fg=frontground)
city.pack(fill=BOTH, expand=1)
city.place(x = 0, y = (h*0.17))

name = Label(root, font=(fontLight),text=json['query']['results']['channel']['item']['condition']['text'], bg=background, fg=frontground)
name.pack(fill=BOTH, expand=1)
name.place(x = (w*0.86), y = (h*0.13))

date = Label(root, font=(fontLight),text=json['query']['results']['channel']['item']['condition']['date'], bg=background, fg=frontground)
date.pack(fill=BOTH, expand=1)
date.place(x = 0, y = (h*0.13))

faren = json['query']['results']['channel']['item']['condition']['temp']
cloud = (float(faren) - 32) / 1.8
cloudy = int(cloud)
temp = Label(root, font=(fontBold),text= str(cloudy) + "°C".decode('utf8'), bg=background, fg=frontground)
temp.pack(fill=BOTH, expand=1)
temp.place(x = (w*0.855), y = 0)


tick()

root.mainloop()

