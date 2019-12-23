import tweepy
import logging
from config import create_api
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("UserjGjYGfek91BO8LNbrbucH",
                           "dOBiadndrxNB05iOhYfeiWbI6LmBxBfMuhnbqDsBD6eHWdQrn6")
auth.set_access_token("972133585753747456-SNNu5Ol8IC8jHs3AOOAZxJconiyzDr7",
                      "ECLRViSaMrAI4EyhI1EmccY2ObhnTIzsgTfInnV0hDjdJ")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()