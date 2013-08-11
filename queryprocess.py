#!/bin/bash

import wolframalpha
import sys
import os
import subprocess
from chatterbot import ChatterBotFactory, ChatterBotType

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID, go and get your own, instructions on my blog.
app_id='6XRJP6-E45RHG32RR'
client = wolframalpha.Client(app_id)
query = ' '.join(sys.argv[1:])

# Check for custom situations
who = {"who are you", "what is your name", "whats your name"}
for x in who:
    if x in query:
        print "I am Jarvis"
        sys.exit() 

#Play Movies
movie = {"play movie"}
for x in movie:
    if x in query:
        directory = '/media/craig/Movies/'
        movie_name = query.replace(x, "")
        movie_name = movie_name.lstrip().title()
        mv_dir = directory + movie_name
        if os.path.isdir(directory + movie_name):
            biggest = ("", -1)
            for item in os.listdir(mv_dir):
                item = mv_dir + "/" + item
                itemsize = os.path.getsize(item)
                if itemsize > biggest[1]:
                    biggest = (item, itemsize)

            if biggest[1] > -1:
                print "Playing " + movie_name
                file_path = biggest[0].replace(" ", "\ ")
                file_path = file_path.replace("(", "\(")
                file_path = file_path.replace(")", "\)")
                os.system("mplayer -vo xv -fs -stop-xscreensaver -zoom " + file_path + "</dev/null>/dev/null  2>&1 &")
                sys.exit()
        else:
            print "I do not have that movie"
            sys.exit()
#Play Music
music = {"play music", "tunes", "jam"}
for x in music:
    if x in query:
        print "Playing music"
        os.system("banshee --play");
        sys.exit()           

#Stop Music
music_stop = {"stop music", "quiet"}
for x in music_stop:
    if x in query:
        print "Stopping Music"
        os.system("banshee --stop")
        sys.exit()

# If custom situations don't exist, ask wolfram alpha
res = client.query(query)
if len(res.pods) > 0:
    texts = ""
    pod = res.pods[1]
    if pod.text:
        texts = pod.text
    else:
        print "I do not have an answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    print texts
else:
    # If all else fails, ask Clever Bot
    factory = ChatterBotFactory()

    bot1 = factory.create(ChatterBotType.CLEVERBOT)
    bot1session = bot1.create_session()

    print bot1session.think(query)
