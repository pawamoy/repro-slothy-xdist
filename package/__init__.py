from slothy import lazy_importing

with lazy_importing():
    from package.kind import Kind
    from package.thing import Thing, make_thing


__all__ = ["Kind", "Thing", "make_thing"]
