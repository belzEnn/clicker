from fastapi import FastAPI

app = FastAPI()

clicks_count = 0

@app.get("/clicks")
async def get_clicks():
    return {"clicks": clicks_count}

@app.post("/click")
async def make_click():
    global clicks_count
    clicks_count += 1
    return {"status": "success", "clicks": clicks_count}