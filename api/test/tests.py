from rest_framework import status


def test_login(api_client):
    response = api_client.post(
        "/login", data={"email": "asdfdadfadf@adf.ru", "password": "incorrect_password"}
    )
    assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY, response.json()


def test_sites(api_client, auth_headers):
    response = api_client.get("/driver", **auth_headers)
    assert response.status_code == status.HTTP_200_OK, response.json()
