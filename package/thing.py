from package.kind import Kind


class Thing:
    kind = Kind.value


def make_thing():
    return Thing()
