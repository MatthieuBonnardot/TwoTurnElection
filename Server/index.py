from fastapi import FastAPI

app = FastAPI()


@app.get("/news/{candidate_name}")
async def read_item(candidate_name):
    return {"candidate_name": candidate_name}
