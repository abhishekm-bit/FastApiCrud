from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_api():
    payload = {
        "url": "https://www.coursera.org",
        "course": "Data Science",
        "level": "Beginner",
        "duration": "1 Month"
    }

    response = client.post("/api/generate", json=payload)

    assert response.status_code == 200
    assert "syllabus" in response.json()
