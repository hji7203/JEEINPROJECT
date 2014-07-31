from flask import Flask, render_template, request
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs
import urllib2
import json
import tweepy

app = Flask(__name__)
app.config['DEBUG'] = True


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@app.route('/idea1.html')
def idea_page():
    """Return a friendly HTTP greeting."""
    return render_template('idea1.html')

@app.route('/webtoon.html')
def webtoon():
	data = urlopen('http://comics.nate.com/webtoon/detail.php?btno=64174')
	soup = BeautifulSoup(data)
	img = []
	for i in soup.select(".toonView img"):
		img.append(i.get('src').encode("utf-8"))
	return render_template('webtoon.html', message = img)


@app.route('/tweet', methods=['GET','POST'])
def tweet():
	if request.method == 'POST':
		consumer_key = 'vShJjEI8pv3q9gt0aSi7SKc8g'
		consumer_secret = 'XJS21YTI4lFxUXGvRJUtDXjt9pUEOwDPaUtLeDNhxzAuBcksh9'
		access_token = '2687234058-fLBbVzQcCDBdCF26UJZ1IWZk2L53A0IZtT2Qaar'
		access_token_secret = 'asPUOYtKi1mywYU33ERqbgPbuTI78pbSal0I4ZjwuMvUs'
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		# Creation of the actual interface, using authentication
		api = tweepy.API(auth)
		tweet_box = request.form['tweet_box']
		# Sample method, used to update a status
		result = []
		for tweet in tweepy.Cursor(api.search,
                       q=tweet_box,
                       rpp=100,
                       result_type="recent",
                       include_entities=True,
                       lang="en").items(10):
			info = {'user' : tweet.user.screen_name ,'content' : tweet.text }
			result.append(info)
		return json.dumps(result)
	else :
		return render_template('tweet.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404















