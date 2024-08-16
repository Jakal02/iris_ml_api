import pytest
from httpx import AsyncClient, Response


@pytest.mark.anyio
async def test_index_route(client: AsyncClient):
    """Test the index route of the API."""
    response: Response = await client.get("/")

    assert response.json() == {"message": "service is online"}
