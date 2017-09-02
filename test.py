from rifmach import replace


def test_rifmach():
    for source, expectation in [
        ("врач", "хуяч"),
        ("бумага", "хуемага"),
    ]:
        yield check_rifmach, source, expectation


def check_rifmach(source: str, expectation: str):
    assert replace(source) == expectation