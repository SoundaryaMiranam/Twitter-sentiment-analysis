# PURPOSE
It helps you monitor and understand people's emotions and the way they are feeling on Twitter.Sentiment analysis involves classifying opinions in text into categories like "positive" or "negative" or "neutral".

# OVERVIEW
# Twitter API
1. Register for the Twitter API https://apps.twitter.com/
2. Create an app  to generate various keys associated with the API. 

handles the Twitter API - tweepy library
Tweepy supports OAuth authentication. Authentication is handled by the tweepy.OAuthHandler class.An OAuthHandler instance is created by passing a consumer token and secret.On this auth instance, a function set_access_token by passing the access_token and access_token_secret.


# Sentiment analysis - Textblob library
It is the process of determining the emotion of the writer, whether it is positive or negative or neutral.sentiment analysis with textblob is Lexicon-based(rule-based) method which defines a list of positive and negative words.

Textblob returns two properties polarity and subjectivity.
1. Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. 
2. subjectivity refers that mostly it is a public opinion and not a factual information.Subjectivity is also a float which lies in the range of [0,1].


