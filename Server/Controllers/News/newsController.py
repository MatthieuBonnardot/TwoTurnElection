#newsapi key : a4dbcea9ba9148ef8c64560a5fc8fa83
from datetime import date
import requests
import json 
#https://newsapi.org/v2/top-headlines?country=fr&category=politic&language=fr&apiKey=a4dbcea9ba9148ef8c64560a5fc8fa83
# get news
def getNews(candidate_name) :  
    news = requests.get("https://newsapi.org/v2/everything?q="+ candidate_name +"&language=fr&apiKey=a4dbcea9ba9148ef8c64560a5fc8fa83")
    return news.json()

# cleanup news
def cleanNews (candidate_news) :
    return candidate_news

# get news by candidate name
def getCandidateNews(candidate_name) :
    candidate_news = getNews(candidate_name)
    formatted_news = cleanNews(candidate_news)
    return formatted_news

