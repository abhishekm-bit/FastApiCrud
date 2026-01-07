import pytest
from httpx import AsyncClient
from httpx import ASGITransport

from Crud_FastApi.main import app
from Crud_FastApi.database import collection


@pytest.mark.asyncio
async def test_create_user():
    collection.delete_many({})

    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/users",
            json={
                "name": "Abhishek",
                "email": "abhi@gmail.com",
                "age": 21
            }
        )

    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"


@pytest.mark.asyncio
async def test_get_users():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_user():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.put(
            "/users/abhi@gmail.com",
            json={
                "name": "Abhishek Updated",
                "email": "abhi@gmail.com",
                "age": 22
            }
        )

    assert response.status_code == 200
    assert response.json()["message"] == "User updated"


@pytest.mark.asyncio
async def test_delete_user():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.delete("/users/abhi@gmail.com")

    assert response.status_code == 200
    assert response.json()["message"] == "User deleted Successfully..."
