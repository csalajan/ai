#!/usr/bin/python

import wolframalpha
import sys

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

# If custom situations don't exist, ask wolfram alpha
res = client.query(query)
if len(res.pods) > 0:
    texts = ""
    pod = res.pods[1]
    if pod.text:
        texts = pod.text
    else:
        texts = "I have no answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    print texts
else:
    print "Sorry, I am not sure."
