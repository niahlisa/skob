import pytest

from authz import create_app

@pytest.fixture  # add a feature to pytest.
def app(): # creat instance,
    app = create_app()
    return app

@pytest.fixture
def client(app): # create ability to test the application.
    return app.test_client()