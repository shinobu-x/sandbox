import tweepy
if __name__ == '__main__':
    key='Qp6jw4KxTawggSGKHAKZkJ27d'
    key_secret='bsGyucNBvP3cbfLbx8PC8SIZVbLAd6GCZ2Lyc5F6oHcqqVcvnU'
    token='845328215937724416-VW1FJtXevKlYaNIGXRbe7OjMUFytxNn'
    token_secret='3jR86G44BgzoZQv3Nc6U95Qt5iy8zi4VVJh5mvgl63nu5'
    auth=tweepy.OAuthHandler(key,key_secret)
    auth.set_access_token(token,token_secret)
    api=tweepy.API(auth,wait_on_rate_limit=True)
    hashtag='#cvpr2022 -filter:retweets'
    #stream=Listener(key,key_secret,token,token_secret)
    #stream=tweepy.Stream(auth,listener)
    #stream.filter(track=[hashtag])
    tweets=[]
    for tweet in tweepy.Cursor(api.search_tweets,q=hashtag,count=100,lang='en').items():
        tweets.append(tweet.text)
    print(len(tweets))
    for tweet in tweets:
        if 'accepted' and 'http' in tweet.lower():
            print(f'{tweet}\n\n')
