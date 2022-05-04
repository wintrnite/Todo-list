import pytest

from app import routes


@pytest.fixture()
def todo_list_mock():
    list_mock = [
        {'finished': False, 'description': 'do homework'},
        {'finished': False, 'description': 'wash dishes'},
        {'finished': False, 'description': 'wash hands'},
        {'finished': False, 'description': 'make breakfast'},
        {'finished': False, 'description': 'make lunch'},
        {'finished': False, 'description': 'make dinner'},
        {'finished': False, 'description': 'drink coffee'},
    ]
    routes.todo_list = list_mock
    return list_mock


@pytest.fixture(scope='session')
def client():
    test_client = routes.app.test_client()
    return test_client
