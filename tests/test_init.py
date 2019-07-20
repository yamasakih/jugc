import pkg_resources

import pytest

import library_template


def test_version() -> None:
    expect = pkg_resources.get_distribution('library_template').version
    actual = library_template.__version__
    assert expect == actual


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
