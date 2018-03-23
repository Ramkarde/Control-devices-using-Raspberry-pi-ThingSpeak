#!/usr/bin/env python
import urllib.request,json,urllib.parse
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED=17
GPIO.setup(LED, GPIO.OUT)
READ_API_KEY='YOUR_ThingSpeak_Read_Key'
CHANNEL_ID= YOUR CHANNEL ID
while True:
    url =("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
    f = urllib.request.urlopen(url)
    data=f.read().decode("latin1")
    pin=int(data[11])
    if pin==1:
        GPIO.output(17,True)
    else:
        GPIO.output(17,False)


