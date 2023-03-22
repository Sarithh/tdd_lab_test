from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_read_call_name():
    name = "sarith"
    response = client.get(f"/callname/{name}")
    assert response.status_code == 200
    assert response.json() == {"Hello": name}

def test_post_call_name():
    name = "sarith"
    response = client.post("/callname", json={'name': name})
    assert response.status_code == 200
    assert response.json() == {"Hello": name}
