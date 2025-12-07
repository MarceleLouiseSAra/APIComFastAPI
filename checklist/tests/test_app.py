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


def test_create_user():
    client = TestClient(app)  # Arrange (organização)

    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'max',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    # Validar UserPublic
    response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'max',
        'email': 'test@test.com',
        'id': 1,
    }
