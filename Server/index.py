from fastapi import FastAPI
from Controllers.News.newsController import getCandidateNews
app = FastAPI()


@app.get("/news/{candidate_name}")
def read_item(candidate_name):
    news = getCandidateNews(candidate_name)
    return news
