from fastapi import FastAPI

app = FastAPI()


@app.get("/news/C1") #Route to the latest news about the candidate 1(= C1)
async def root():
    return "Here are the latest news about the C1"

@app.get("/news/C2") #Route to the latest news about the candidate 2(= C2)
async def root():
    return "Here are the latest news about the  C2"