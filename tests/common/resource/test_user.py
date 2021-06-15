import pytest

from json import dumps
@pytest.mark.parametrize(
    ("data", "headers", "status"),
    [
        ({}, {}, 415),
        ({}, {"Contecnt-Type": "application/json"}, 400),
        ({"": ""}, {"Contecnt-Type": "application/json"}, 400),
        ({"user": "test", "pass": "test"}, {"Contecnt-Type": "application/json"}, 400),
        ({"username": "test", "password": "test", "key": "test"}, {"Contecnt-Type": "application/json"}, 400),
        ({"username": "", "password": ""}, {"Contecnt-Type": "application/json"}, 400),
        ({"username": "test", "password": "test"}, {"Contecnt-Type": "application/json"}, 201),
        ({"username": "test", "password": "test"}, {"Contecnt-Type": "application/json"}, 409)
    ]
)
def test_create_user(client, data, headers, status):
    result = client.post(
        "/users",
        data=dumps(data),
        headers=headers
    )
    assert result.status_code == status # dynamic- check she status code umade ba un 415 yeki hast ya na.

