import json

import mock
import pytest

import lightbulb


@pytest.fixture
def client():
    lightbulb.app.config['TESTING'] = True
    return lightbulb.app.test_client()


def test_dummy_endpoint(client):
    r = client.get('/echo')
    assert 'Hello World!' == r.data
    assert r.status_code == 200


def test_sensors_endpoint(client):
    with mock.patch('lightbulb.sensors.fetch_data', return_value={}):
        r = client.get('/sensors')
    assert {} == json.loads(r.data)
    assert r.status_code == 200


def test_dashboard_endpoint(client):
    r = client.get('/')
    assert r.status_code == 200
