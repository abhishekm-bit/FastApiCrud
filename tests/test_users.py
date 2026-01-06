import pytest
from httpx import AsyncClient
from CRUD_FASTAPI.main import app

from database import collection


@pytest.mark.asyncio
async def test_create_user():
    # cleanup before test
    collection.delete_many({})

    async with AsyncClient(app=app, base_url="http://test") as ac:
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/users/abhi@gmail.com")

    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"
