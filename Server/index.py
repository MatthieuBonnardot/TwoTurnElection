from fastapi import FastAPI
from Controllers.News.newsController import getCandidateNews
app = FastAPI()


@app.get('/sentiment/{candidate_name}')
async def getSentiment(candidate_name):
    
    return { 'Sentiment' : candidate_name }


@app.get("/news/{candidate_name}")
def read_item(candidate_name):
    news = getCandidateNews(candidate_name)
    return news

