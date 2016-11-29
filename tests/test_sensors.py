import mock

import lightbulb


class SensorMock(object):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def name(self):
        return self._name

    def value(self):
        return self._value


def test_fetch_all_empty():
    with mock.patch('lightbulb.sensors.REGISTRY', new=set()):
        assert {} == lightbulb.sensors.fetch_data()


def test_fetch_all_something():
    with mock.patch('lightbulb.sensors.REGISTRY', new={SensorMock('name', 1)}):
        assert {'name': 1} == lightbulb.sensors.fetch_data()


def test_registry():
    registry = set()
    with mock.patch('lightbulb.sensors.REGISTRY', new=registry):
        s1 = lightbulb.sensors.register(SensorMock('first', 1))
        assert len(registry) == 1
        assert s1 in registry

        s2 = lightbulb.sensors.register(SensorMock('second', 2))
        assert len(registry) == 2
        assert s2 in registry

        lightbulb.sensors.deregister(s1)
        assert s1 not in registry
        assert s2 in registry


def test_deregister_all():
    registry = set()
    with mock.patch('lightbulb.sensors.REGISTRY', new=registry):
        lightbulb.sensors.register(SensorMock('first', 1))
        lightbulb.sensors.register(SensorMock('second', 2))
        assert len(registry) == 2
        lightbulb.sensors.deregister_all()
        assert len(registry) == 0
