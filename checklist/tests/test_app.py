from http import HTTPStatus

from fastapi.testclient import TestClient

from src.checklist.app import app


def test_read_root_deve_retornar_ok_e_as_boas_vindas():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (garantia)
    assert response.json() == {
        'message': 'Welcome to the Checklist API!'
    }  # Assert
