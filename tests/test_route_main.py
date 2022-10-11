from fastapi.testclient import TestClient
from source.main import app
client = TestClient(app)

# Teste main
def test_run():
    response = client.get("/")
    assert response.status_code == 200


