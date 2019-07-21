import pkg_resources

import pytest

import jugc


def test_version() -> None:
    expect = pkg_resources.get_distribution('jugc').version
    actual = jugc.__version__
    assert expect == actual


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
