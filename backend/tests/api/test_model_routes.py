import pytest
from httpx import AsyncClient, Response


@pytest.mark.anyio
async def test_is_fit_route(client: AsyncClient):
    """Test that the model returns is_fit."""
    response: Response = await client.get("/model/is_fitted")

    assert response.json() == {"model status": True}
