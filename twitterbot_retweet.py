import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets, like tweets, replies to tweets, and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

count = 0
for tweet in tweepy.Cursor(api.search_tweets, q=QUERY).items():
    if count == 15:
        break
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # tweet.retweet()
        # print('Retweeted the tweet')

        status = "Hey! Feel free to give this book a try " \
                 "https://www.amazon.com/Dirty-Lovers-poetry-prose-heart/dp/B08Y4RLXP5/ref=sr_1_1?keywords=cole" \
                 "+goddard&qid=1658785953&sprefix=cole+go%2Caps%2C113&sr=8-1 @" + tweet.user.screen_name

        api.update_status(status=status)
        print('Replied to tweet')

        # Favorite the tweet
        if LIKE:
            if not api.get_favorites():
                tweet.favorite()
            print('Favorited the tweet')

        # Follow the user who tweeted
        # check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')
        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
