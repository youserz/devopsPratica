from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == "Hello World 2"


def test_unknown_route():
    assert client.get("/inexistente").status_code == 404


def test_hello_rejects_post():
    assert client.post("/hello").status_code == 405
