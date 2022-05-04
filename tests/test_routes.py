import pytest
from requests import codes

from app import routes
from app.constants import QueryParams


@pytest.mark.parametrize('url', ['/', '/?status=finished', '/?status=active'])
def test_base_route(url: str, client):
    response = client.get(url)
    assert response.status_code == codes['OK']


def test_add_task(client, todo_list_mock):
    start_length_todo_list = len(todo_list_mock)
    url = '/'
    response = client.post(url, data={'task': 'do push-ups'})
    assert len(routes.todo_list) == start_length_todo_list + 1
    assert response.status_code == codes['OK']


def test_add_task_bad(client, todo_list_mock):
    url = '/'
    response = client.post(url, data={'work': 'do push-ups'})
    assert response.status_code == codes['bad_request']


def test_finish_task(client, todo_list_mock):
    testing_index = 0
    url = f'/finish_task?index={testing_index}'
    response = client.post(url)
    assert response.status_code == codes['OK']
    assert routes.todo_list[testing_index]['finished']


def test_finish_not_exist_task(client, todo_list_mock):
    url = f'/finish_task?index={len(todo_list_mock) + 1}'
    response = client.post(url)
    assert response.status_code == codes['bad_request']


def test_filter_tasks(client, todo_list_mock):
    response_with_all_tasks = client.get(
        '/', query_string={QueryParams.filter_substring.value: 'do'}
    )
    assert response_with_all_tasks.status_code == codes['OK']

    response_with_finished_tasks = client.get(
        '/',
        query_string={
            QueryParams.filter_substring.value: 'do',
            QueryParams.task_status.value: 'finished',
        },
    )
    assert response_with_finished_tasks.status_code == codes['OK']

    response_with_active_tasks = client.get(
        '/',
        query_string={
            QueryParams.filter_substring.value: 'do',
            QueryParams.task_status.value: 'active',
        },
    )
    assert response_with_active_tasks.status_code == codes['OK']
