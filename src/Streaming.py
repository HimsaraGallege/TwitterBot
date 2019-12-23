import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("UserjGjYGfek91BO8LNbrbucH",
                           "dOBiadndrxNB05iOhYfeiWbI6LmBxBfMuhnbqDsBD6eHWdQrn6")
auth.set_access_token("972133585753747456-SNNu5Ol8IC8jHs3AOOAZxJconiyzDr7",
                      "ECLRViSaMrAI4EyhI1EmccY2ObhnTIzsgTfInnV0hDjdJ")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])