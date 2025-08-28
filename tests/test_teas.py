# tests/test_teas.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from models.user import UserModel
from models.tea import TeaModel
from tests.lib import login
from main import app

def test_get_teas(test_app: TestClient, override_get_db):
    response = test_app.get("/api/teas")
    assert response.status_code == 200
    teas = response.json()
    assert isinstance(teas, list)
    assert len(teas) >= 2  # Ensure there are at least two teas in the test database
    for tea in teas:
        assert 'id' in tea
        assert 'name' in tea
        assert 'in_stock' in tea
        assert 'rating' in tea
        assert 'user' in tea
        assert 'email' in tea['user']
        assert 'username' in tea['user']

