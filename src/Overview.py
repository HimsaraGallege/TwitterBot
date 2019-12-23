import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("UserjGjYGfek91BO8LNbrbucH",
                           "dOBiadndrxNB05iOhYfeiWbI6LmBxBfMuhnbqDsBD6eHWdQrn6")
auth.set_access_token("972133585753747456-SNNu5Ol8IC8jHs3AOOAZxJconiyzDr7",
                      "ECLRViSaMrAI4EyhI1EmccY2ObhnTIzsgTfInnV0hDjdJ")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Methods for user timelines
timeline = api.home_timeline()
# for tweet in timeline:
    # print(f"{tweet.user.name} said {tweet.text}")

# Methods for tweets
# api.update_status("Test tweet from Tweepy Python")

# Methods for Users
user = api.get_user("MendisVimuth")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

# Methods for Followers
api.create_friendship("realpython")

# Methods for Account
api.update_profile(description="I like Python")

# Methods for Likes
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# Methods for Blocking Users
for block in api.blocks():
    print(block.name)

# Methods for Searches
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

# Methods for Trends
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])


