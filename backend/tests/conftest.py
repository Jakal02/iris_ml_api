"""Test configuration file 

It's existance is automatically detected by pytest.
"""
from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app


@pytest.fixture(scope="function")
async def app_manager():
    async with LifespanManager(app) as manager:
        yield manager.app


@pytest.fixture
def anyio_backend() -> str:
    """Clarify asyncio as backend for all pytest.mark.anyio decorators."""
    return "asyncio"

@pytest.fixture(scope="function")
async def client(app_manager) -> AsyncGenerator[AsyncClient, None]:
    """Return an AsyncClient of the FastAPI app for every pytest function."""
    async with AsyncClient(
        transport=ASGITransport(app=app_manager), base_url="https://test/"
    ) as c:
        yield c

