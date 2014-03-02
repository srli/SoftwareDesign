# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:52:17 2014

@author: sophie
"""
from pattern.en import *
from pattern.web import *
import webcolors
from random import randint
import Image


bad_words=['a','the','at','be','to','of','and','that','it','for','this','RT','@','http','is']
#facebook id = CAAEuAis8fUgBAN77AyE2NDJho0JJnP0ZBraJ5h7qmUwZBdtgJPeWb7tLSzg0NhxhDXBECuzmIKs11kujOnyfizyGxDgSlSB3OOiCMJYdCTTP7g9uarYGBCZC5t9HhDbHBdSo4HWGbOkIYX0MshCQT93BucAc0B3xKLUwZBmfsNoLuvLv3Pk6

def twitter_call(hashtag,tweet_numbers):
    """Seaches twitter for the latest x tweets with the provided hashtag. Returns
    results in stream_tweet with no changes"""
    t = Twitter()
    i = None
    stream_tweet = []
    for j in range(3):
        for tweet in t.search(hashtag, start=i, count=tweet_numbers):
            stream_tweet.append(tweet.text)
    return stream_tweet

#note that we can query multiple hashtags
#print twitter_call('sunny', 10)

def twitter_sentiment(hashtag):
    """Generates sentiment from tweets. Strips out general words for more accurate sentiment calculations"""
    stream_tweet = twitter_call(hashtag,25)
    clean_twitter = []
    twitter_sentiment = []
    i = 0
    while i < len(stream_tweet):
        tweet = stream_tweet[i]
        tweet_words = tweet.split(' ')
        #I'm unsure of how to strip the @ handles and URL's, we'll generalize to say most of these appear at the beginning and end of tweets
        tweet_words = tweet_words[2:-1]
        clean_tweet = ' '.join([j for j in tweet_words if j not in bad_words])
        if sentiment(clean_tweet)[0] != 0:
            twitter_sentiment.append(sentiment(clean_tweet))
        clean_twitter.append(clean_tweet)
        i += 1
    return twitter_sentiment

#print twitter_sentiment()

    
def facebook_call(post_numbers):
    """Searches facebook for lastest x posts and outputs to stream_facebook with no
    analysis."""
    fb = Facebook(license='CAAEuAis8fUgBAMYOWhpc1qRQ8ZAdWcCzyPqGBoqFihnKvumPmrStYrCxAEyHIEa26eycDVsNc7IIfnba0G9ueBlnAlpmlduElck47h46heP0AijyjhM10Heqzf2fWNQy8UZBLCwGM8Xoobxcrac3lhVzhoB2iQYF49jMCpXsNPeUEM4bfCxomQZBal7NWQZD', throttle=0.5)
    me = fb.profile(id=None) # (id, name, date, gender, locale, likes)-tuple
    stream_facebook = []
    for post in fb.search(me[0], type=NEWS, count=post_number):
        stream_facebook.append(post.text)
    return stream_facebook
   
#print facebook_call(20)

#test_list=['Hello world!','Sophie Li says Hello World!','Junebug posted on your wall','Samuel Adames liked your post','This is odd']

def facebook_sentiment():
    stream_facebook = facebook_call(100)
    bad_list=['Sophie Li','wall','post','timeline']
    while i < 4:
        if bad_list[i] in stream_facebook:
            i += 1
    delete_fluffy = []
    for r in len(stream_facebook):
        stream_facebook

def sentiment_average(source_sentiment):
    """Takes list of all sentiments from twitter and facebook and averages"""
    positivity_total = 0
    subjectivity_total = 0
    i = 0
    while i < len(source_sentiment):
        positivity_total = positivity_total + source_sentiment[i][0]
        subjectivity_total = subjectivity_total + source_sentiment[i][1]
        i += 1
    sentiment_average = [positivity_total/len(source_sentiment), subjectivity_total/len(source_sentiment)]
    return sentiment_average

#print sentiment_average(twitter_sentiment())

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        Using math, we can find the formula necessary for remappying a value to another interval.
        Supposing we have a range [min,max] and we want to scale it to [a,b]
        
               (b-a)(x-min)
        f(x) = ------------  + a
                  max-min
    """
    output_interval = output_interval_end - output_interval_start
    output_interval = float(output_interval)
    input_interval = input_interval_end-input_interval_start
    scaled_val = (output_interval*(val - input_interval_start)/(input_interval)) + output_interval_start
    return scaled_val

def closest_colour(requested_colour):
    """Generates RGB values that are closest to the ones in webcolor. Delivers answer by Euclidian distance in RGB space
    This function and get_colour_name were taken from fraxel on stackoverflow. 
    URL to answer is: http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green"""
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    """Outputs colosest english color name to input RGB"""
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def pyscho_pass():
    """Pulls sentiment info in from twitter or Facebook. Generates an RGB color tile depending on general
    sentiment in info"""
    sentiment = sentiment_average(twitter_sentiment('life'))
    green = remap_interval(sentiment[1],-1,1,0,255)
    if sentiment[1] > 0.6:        
        blue = randint(200,255)
    else:
        blue = randint(100,200)
    if sentiment[0] > 0.25:
        red = remap_interval(sentiment[0],0,1,200,255)
    else:
        red = remap_interval(sentiment[0],0,1,0,200)
    color = (int(red),int(green),int(blue))
    actual_name, closest_name = get_colour_name(color)
    print "General hue is",closest_name
    print "Sentiment analysis displays", sentiment
    img = Image.new("RGB", (350,350),color) #we designate size of image here
    img.show()

pyscho_pass()



#print "Actual colour name:", actual_name, ", closest colour name:", closest_name
#print closest_name