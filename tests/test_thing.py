import pytest

from package import Kind, make_thing

def test_enum_value():
    thing = make_thing()
    assert thing.kind is Kind.value


@pytest.mark.parametrize("carlmeyer", range(1000))
def test_carl_meyer(carlmeyer):
    assert carlmeyer == carlmeyer
    assert carlmeyer == carlmeyer
    assert carlmeyer == carlmeyer
