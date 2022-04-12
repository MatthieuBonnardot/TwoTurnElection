import pymongo
from time import sleep
from webbrowser import get
from tqdm import tqdm
import requests


api_token =  'AAAAAAAAAAAAAAAAAAAAAEj1bAEAAAAAeboOzfaCGiz0HGgH5w4f8rjEFTA%3Dp2YjLo1AxSUHPcdvCWgHz0DCBnLYAcrlDilg6Uok15q7hypmAy'
search_url = "https://api.twitter.com/2/tweets/search/recent"
client = pymongo.MongoClient("mongodb+srv://admin:admin@twoturncluster.jej2t.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


def getMongoClient(col):
    db = client['TwoTurn']
    return db[col]

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {api_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def getTweets(candidate_name):
    print('Fetching Tweets for ' + candidate_name)
    next_token = ''
    local_storage = []
    for i in tqdm(range(250)):
        if i == 60 or i == 120:
            print('Cooling down for request limit!')
            sleep(60)
        if next_token == '':
            query_params = {'query' : candidate_name + ' lang:FR', 'max_results' : 100}
        else:
            query_params = {'query' : candidate_name + ' lang:FR', 'max_results' : 100, 'next_token' : next_token}
        result = connect_to_endpoint(search_url, query_params)
        for tweet in result['data']:
            local_storage.append({
                "text": tweet['text']
            })
        next_token = result['meta']['next_token']
    return local_storage



def storeTweetsInDB(cleaned_tweets, candidate_name):
    try:
        getMongoClient(candidate_name).insert_many(cleaned_tweets)
    except Exception as e:
        print(e)
        

def getTweetsPerCandidate(candidate_name):
    try:
        candidate_tweets = getTweets(candidate_name)
        storeTweetsInDB(candidate_tweets, candidate_name)
    except Exception as e:
        print(e)
        
        
getTweetsPerCandidate('macron')
getTweetsPerCandidate('marinelepen')