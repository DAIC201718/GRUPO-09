#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import tweepy  
from subprocess import call  
from datetime import datetime  
def Photo(photo_name):
	print(photo_name)
	# Consumer keys and access tokens, used for OAuth  
	consumer_key = 'LSgXRTcPrqCrA93GkJEQiYFr9'
	consumer_secret = 'aX0pfvEgEsWy81oM2KY7j0I6MQgYQ9tJWN50UHImSJEZQ7Yls7'
	access_token = '956506082377195520-dKO6N0KHGygP1p0Yh1vsENJPwV1WrWt'
	access_token_secret = 'iFad3BtGaYSMawv57u107PlueIvhDyINw7ve5D3EpDZuw'
  
	# OAuth process, using the keys and tokens  
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
	auth.set_access_token(access_token, access_token_secret)  
   
	# Creation of the actual interface, using authentication  
	api = tweepy.API(auth)  
  
	# Send the tweet with photo  
	photo_path =('/home/pi/labDAIC/multones/'+str( photo_name))
	status =  '@dieguich semaforoIOT'
	api.update_with_media(photo_path, status=status)


