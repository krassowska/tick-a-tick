from flask import Flask, render_template, request
from app import app
import tweepy
import os

consumer_key = os.environ.get('twitter_consumer_key', None)
consumer_secret = os.environ.get('twitter_consumer_secret', None)
access_token = os.environ.get('twitter_access_token', None)
access_token_secret = os.environ.get('twitter_access_token_secret', None)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route('/news', methods=["GET"])
def news():
    #twitter_names =
    #for name in twitter_names:
    tweets_from_timeline = api.user_timeline(screen_name='Lymenews', count=5)
    return render_template('home.html', tweets_from_timeline=tweets_from_timeline)

#@app.route('/tweet', methods=["POST"])
#def tweet():
#    text = request.form['Tweet']
#    post_tweet = api.update_status(text)
#    response = f"Your tweet was send: {text}"
#    return render_template('main.html', response=response)