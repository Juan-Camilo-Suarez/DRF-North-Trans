import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from api.test.factories import UserFactory


@pytest.fixture(autouse=True)
def enable_db_for_all_tests(db):
    pass


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_headers():
    user = UserFactory
    token = Token.objects.create(user=user)
    return {"HTTP_AUTHORIZATION": f"Token {token.key}"}
