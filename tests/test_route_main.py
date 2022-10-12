from fastapi.testclient import TestClient
from source.main import app
import logging

client = TestClient(app)

logging.basicConfig(level=logging.INFO, filename= "route_tests.log")

# Teste main
def test_run():
    response = client.get("/")
    assert response.status_code == 200


