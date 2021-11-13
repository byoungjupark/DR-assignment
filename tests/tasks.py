from tests.database import client


def test_create_task_success():
    response = client.post(
        "task/",
        json = {"id":1, "name":"test", "completed":False}
    )
    assert response.status_code == 200

def test_create_task_fail_validation():
    response = client.post(
        "task/",
        json = {"name":"test"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "ValidationError"}


def test_get_all_tasks_success():
    response = client.get("task/")
    assert response.status_code == 200
    assert response.json() == [{
        "id"       : 1,
        "name"     : "test",
        "completed": False
    }]


def test_get_task_success():
    response = client.get("task/1")
    assert response.status_code == 200
    assert response.json() == {
        "id"       : 1,
        "name"     : "test",
        "completed": False
    }

def test_get_task_fail_non_data():
    response = client.get("task/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_update_task_success():
    response = client.patch(
        "task/1",
        json = {"name":"change"}
    )
    assert response.status_code == 200


def test_update_task_fail_validation():
    response = client.patch(
        "task/1",
        json = {"name":""}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "ValidationError"}


def test_update_task_fail_non_data():
    response = client.patch(
        "task/2",
        json = {"name":"change"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_delete_task_success():
    response = client.delete("task/1")
    assert response.status_code == 200


def test_delete_task_fail_non_data():
    response = client.delete("task/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_delete_all_tasks_success():
    client.post(
        "task/",
        json = {"name":"test2", "completed":False}
    )
    response = client.delete("task/")
    assert response.status_code == 200


def test_delete_all_tasks_fail_non_data():
    response = client.delete("task/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
