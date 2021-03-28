pip install tweepy

pip install textblob

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import tweepy 
from tweepy import OAuthHandler 

from textblob import TextBlob

# keys and tokens from the Twitter Dev Console 
consumer_key = '********************************'
consumer_secret = '******************************************'
access_token = '**********************************************'
access_token_secret = '*******************************************'

# attempt authentication 
try: 
    # create OAuthHandler object 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    # set access token and secret 
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets 
    api = tweepy.API(auth)
except: 
    print("Error: Authentication Failed")

#Extracting 1000 tweets from a subject "Lockdown"
corpus_tweets = api.search("lockdown", count=1000, lang ="en", tweet_mode = "extended")

#print 5 tweets on this subject
i = 1
print("Show recent tweets: \n")
for tweet in corpus_tweets[0:5]:
    print(str(i) + ')' + tweet.full_text  + '\n')
    i = i+1

#Creating adataframe 
df = pd.DataFrame([tweet.full_text for tweet in corpus_tweets] , columns=['Tweets'])
df.head()

#creating function to clean the tweets
def cleantext(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove @mention
    text = re.sub(r'#', '', text)  # remove hash symbols
    text = re.sub(r'RT[\s]+', '', text) # remove RT
    text = re.sub(r'https?:\/\/\s+', '', text) # remove  hyper links

    return text

df['Tweets'] = df['Tweets'].apply(cleantext)
df.head()

#Creating a function to get subjectivity and polarity
def getsubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getpolarity(text):
    return TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(getsubjectivity)

df['Polarity'] = df['Tweets'].apply(getpolarity)
df.head()

#Create function to analyse sentiments
def getanalysis(score):
    if score > 0:
      return 'Positive'
    elif score == 0:
      return 'Neutral'
    else:
      return 'Negative'  

df['Analysis'] = df['Polarity'].apply(getanalysis)
df.head()

#Ploting the sentiment analysis

sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
for i in range(0, df.shape[0]):
   plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color = 'Blue')

plt.title("Sentiment analysis")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.show()

#caluclating the precentages
def percentage(part,whole):
 return 100 * float(part)/float(whole)

positive = df[df['Analysis']== "Positive"]
negative = df[df['Analysis']== "Negative"]
neutral = df[df['Analysis']== "Neutral"]
noOfTweet = df['Tweets'].count()

Positive = percentage(len(positive), noOfTweet)
Negative = percentage(len(negative), noOfTweet)
Neutral = percentage(len(neutral), noOfTweet)
positive_cent = format(Positive, '.1f')
negative_cent = format(Negative, '.1f')
neutral_cent = format(Neutral, '.1f')

#Creating PieCart
labels = ['Positive ['+str(positive_cent)+'%]' , 'Neutral ['+str(neutral_cent)+'%]','Negative ['+str(negative_cent)+'%]']
sizes = [len(positive), len(neutral), len(negative)]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword= lockdown")
plt.axis('equal')
plt.show()

#Creating barplot
labels = df.groupby('Analysis').count().index.values
values = df.groupby('Analysis').size().values
plt.bar(labels, values)
plt.show()
