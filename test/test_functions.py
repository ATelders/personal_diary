import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import *
from fastapi.testclient import TestClient
from src.api.api import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
