import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from website import create_app  # noqa

app = create_app('test')
app.testing = True


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get(client):
    for uri in ['/', '/ml', '/ml/project/mnist', '/ml/demo/mnist']:
        assert client.get(uri, follow_redirects=True).status_code == 200
