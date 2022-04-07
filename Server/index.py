from fastapi import FastAPI

app = FastAPI()


@app.get('/sentiment/c1')
async def getSentimentC1():
    return { 'message' : 'test' }

@app.get('/sentiment/c2')
async def getSentimentc2():
    return { 'message' : 'test2'}