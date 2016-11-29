REGISTRY = set()


def register(sensor):
    REGISTRY.add(sensor)
    return sensor


def deregister(sensor):
    REGISTRY.remove(sensor)


def deregister_all():
    REGISTRY.clear()


def fetch_data():
    return {s.name(): s.value() for s in REGISTRY}
