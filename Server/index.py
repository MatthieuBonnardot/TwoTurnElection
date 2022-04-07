from fastapi import FastAPI

app = FastAPI()



@app.get('/sentiment/{candidate_name}')
async def getSentiment(candidate_name):
    return { 'Sentiment' : candidate_name }


@app.get("/news/{candidate_name}")
async def read_item(candidate_name):
    return {"candidate_name": candidate_name}

