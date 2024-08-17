"""Main for ML Backend."""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from catboost import CatBoostClassifier


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries_db = 60 * 1  # 1 minutes
max_tries_search = 60 * 1
wait_seconds_db = 1
wait_seconds_search = 1


model = CatBoostClassifier()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events.
    
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    global model
    model = model.load_model("./app/final_model_1.0")
    if model.is_fitted():
        logger.info("Model successfully loaded.")
    else:
        logger.warn("Model has not been loaded.")
    yield
    model = None


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root_of_app():
    return {"message": "service is online"}

@app.get("/model/is_fitted")
async def model_is_fitted():
    """Return whether the model is fitted or not."""
    return {"model status": model.is_fitted()}
