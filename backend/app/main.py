"""Main for ML Backend."""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from catboost import CatBoostClassifier
import numpy as np

from app.schemas.observation_schema import ObservationModel, SpeciesEnum, SpeciesModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries_db = 60 * 1  # 1 minutes
max_tries_search = 60 * 1
wait_seconds_db = 1
wait_seconds_search = 1


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events.
    
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    global model
    model = CatBoostClassifier()
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
    global model
    return {"model status": model.is_fitted()}

@app.post("/model/predict")
async def predict_model_species(input: ObservationModel) -> SpeciesModel:
    """Use model to guess species given observation data.

    following the note given 
    [here](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_predict),
    the parameters will follow the following order: the same that they appeared during training:  

    sepal length, sepal width, petal length, petal width
    """
    global model
    obs = [input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]

    result_species = model.predict(obs)[0]

    return SpeciesModel(species=result_species)
