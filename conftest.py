import sys
import os
import pytest
import requests

# Fixed 'file' to '__file__' for path discovery
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))


@pytest.fixture(scope="session")
def base_url():
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def api_session():
    # Creates a session to persist parameters (like cookies/headers) across requests
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    yield session
    # Code after 'yield' runs when the testing session ends
    session.close()


@pytest.fixture(scope="session")
def base_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
