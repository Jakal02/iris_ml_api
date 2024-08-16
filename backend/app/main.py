"""Main for ML Backend."""

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root_of_app():
    return {"message": "service is online"}
