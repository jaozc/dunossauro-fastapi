import pytest
from fastapi import status
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'Bem-vindo à API FastAPI do Zero!',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    }


def test_read_docs(client):
    response = client.get('/docs')
    assert response.status_code == status.HTTP_200_OK


def test_read_redoc(client):
    response = client.get('/redoc')
    assert response.status_code == status.HTTP_200_OK


def test_read_hello_world(client):
    response = client.get('/hello-world')
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello World</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }
                h1 {
                    color: #1a73e8;
                    text-align: center;
                    padding: 20px;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """

    assert response.status_code == status.HTTP_200_OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert response.text.strip() == html_content.strip()


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'password',
        },
    )  # Act

    assert response.status_code == status.HTTP_201_CREATED  # Assert
    assert response.json() == {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'name': 'John Doe',
                'email': 'john.doe@example.com',
            }
        ]
    }


def test_get_single_user(client):
    response = client.get('/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
    }


def test_get_single_user_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        'detail': 'User Not Found',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'name': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_updatde_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User Not Found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'User deleted',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User Not Found'}
