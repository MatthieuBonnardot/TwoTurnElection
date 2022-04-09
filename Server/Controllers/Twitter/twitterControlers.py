from time import sleep
import requests
import json

api_token =  'AAAAAAAAAAAAAAAAAAAAAEj1bAEAAAAAeboOzfaCGiz0HGgH5w4f8rjEFTA%3Dp2YjLo1AxSUHPcdvCWgHz0DCBnLYAcrlDilg6Uok15q7hypmAy'

search_url = "https://api.twitter.com/2/tweets/search/recent"



def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {api_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def getTweets(candidate_name):
    next_token = ''
    local_storage = []
    for i in range(3):
        if i == 60 or i == 120:
            print('cooldown!')
            sleep(20)
        if next_token == '':
            query_params = {'query' : 'macron lang:FR', 'max_results' : 100}
        else:
            query_params = {'query' : 'macron lang:FR', 'max_results' : 100, 'next_token' : next_token}
        result = connect_to_endpoint(search_url, query_params)
        for tweet in result['data']:
            local_storage.append(tweet['text'])
        next_token = result['meta']['next_token']
    return local_storage

def cleanTweetsForProcessing(candidate_tweets):
    return

def storeTweetsInDB(cleaned_tweets):
    return

def getTweetsPerCandidate(candidate_name):
    candidate_tweets = getTweets(candidate_name)
    cleaned_tweets = cleanTweetsForProcessing(candidate_tweets)
    storeTweetsInDB(cleaned_tweets)
    
getTweets('')