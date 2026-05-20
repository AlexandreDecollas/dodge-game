_events: list[dict] = []


def log(event_type: str, **kwargs):
    _events.append({"type": event_type, **kwargs})


def clear():
    _events.clear()


def events():
    return list(_events)
