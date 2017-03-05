# March 5, 2017
# Hacktech2017 - Pasadena,CA
# Russell Caletena, Celestine Co, Alexander Garcia, Josiah Pang, and Samir Shah
# A collaboration of students from California Polytechnic State University - San Luis Obispo and Oregon State University

import tweepy
import random

# print('Welcome to The Twitter Page of Hush Harassment! ')
mode = input('Please choose between "PersonalTweet" or "RandomTweet"')
import sys

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

tconsumer_key = 'Z0HQqEd7vTmszsEa5FOKLqKji'
tconsumer_secret = 'cwCszQqmUYjNaqOeJseDWcRbj01RYnAOyulXU4uYN1CMN1o5XC'
taccess_token = '838289759633997825-f19KbxiGiEbQ3uwASkzcO57wqiqMKrQ'
taccess_token_secret = 'JDoYvCE2jEYN6NbrOGhIoCGiqhxfKCS8ziBriANezglW1'

if (mode == 'PersonalTweet'):
  def main():
    cfg = {
      "consumer_key": tconsumer_key,
      "consumer_secret": tconsumer_secret,
      "access_token": taccess_token,
      "access_token_secret": taccess_token_secret
    }
    personaltweet = input('Enter your tweet here (max 140 characters): ')
    api = get_api(cfg)
    status = api.update_status(status=personaltweet)
    print(" {} has been sent to Twitter.".format(personaltweet))

  if __name__ == "__main__":
    main()

if (mode == 'RandomTweet'):
  def main():
    cfg = {
      "consumer_key"        : tconsumer_key,
      "consumer_secret"     : tconsumer_secret,
      "access_token"        : taccess_token,
      "access_token_secret" : taccess_token_secret
    }

    quoteone = '60% of internet users said they had witnessed someone being called offensive names. #hushharassment'
    quotetwo = '24% witnessed someone being harassed for a sustained period of time. #hushharassment'
    quotethree = 'Young adults are the most likely demographic group to experience harassment online. #hushharassment'
    quotefour = '66% of those who have been harassed cited social media websites and apps. #hushharassment'
    quotefive = '63% of American women online report knowing someone who has been targeted online. #hushharassment'
    quotesix = '62% of people who report harassment experienced it on Facebook, 24% Twitter, 20% via email and 18% YouTube. #hackharassment'
    quotes = [quoteone, quotetwo, quotethree, quotefour, quotefive, quotesix]
    generate_quotes = random.choice(quotes)
    api = get_api(cfg)
    tweet = generate_quotes
    status = api.update_status(status=tweet)
    print(" {} has been sent to Twitter.".format(tweet))

  if __name__ == "__main__":
    main()

