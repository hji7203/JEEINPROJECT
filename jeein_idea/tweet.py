from flask import Flask, render_template, request
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs
import urllib2
import tweepy


consumer_key = 'vShJjEI8pv3q9gt0aSi7SKc8g'
consumer_secret = 'XJS21YTI4lFxUXGvRJUtDXjt9pUEOwDPaUtLeDNhxzAuBcksh9'
access_token = '2687234058-fLBbVzQcCDBdCF26UJZ1IWZk2L53A0IZtT2Qaar'
access_token_secret = 'asPUOYtKi1mywYU33ERqbgPbuTI78pbSal0I4ZjwuMvUs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
# tweet_box = request.form['tweet_box']
# Sample method, used to update a status
for tweet in tweepy.Cursor(api.search,
                           q="google",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    print tweet.created_at, tweet.text
		