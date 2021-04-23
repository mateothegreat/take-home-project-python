import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# @pytest.mark.asyncio
# async def test_root():
#     async with AsyncClient(app=app, base_url="http://localhost") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Hello": "World yeah!!"}
    
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World yeah!!"}