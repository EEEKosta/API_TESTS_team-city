import pytest
import requests
from api.api_manager import ApiManager


@pytest.fixture
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture
def api_manager(session):
    return ApiManager(session)