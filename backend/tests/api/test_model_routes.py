import pytest
from httpx import AsyncClient, Response

from app.schemas.observation_schema import ObservationModel


@pytest.mark.anyio
async def test_is_fit_route(client: AsyncClient):
    """Test that the model returns is_fit."""
    response: Response = await client.get("/model/is_fitted")

    assert response.json() == {"model status": True}

@pytest.mark.anyio
async def test_predict_route(client: AsyncClient):
    """Test that model predicts"""
    data = ObservationModel(sepal_length=5,
                            sepal_width=5,
                            petal_length=5,
                            petal_width=3)

    response: Response = await client.post("/model/predict",
                                           json=data.model_dump())

    assert response.json()['species'] in ["sertosa", "virginica", "versicolor"]
