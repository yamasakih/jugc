import pkg_resources

import pandas as pd
import pytest
from rdkit.Chem import MolFromSmiles

import jugc
from jugc import calculate_descriptors


def test_version() -> None:
    expect = pkg_resources.get_distribution('jugc').version
    actual = jugc.__version__
    assert expect == actual


def test_calculate_descriptors() -> None:
    mol = MolFromSmiles('c1ccccc1')

    descs = calculate_descriptors(mol, names=['MolWt'])

    actual = descs
    expect = pd.Series
    assert isinstance(actual, expect)

    actual = list(descs.index)
    expect = ['MolWt']
    assert actual == expect

    actual = descs.MolWt
    expect = 78.114
    assert pytest.approx(actual, 0.001) == expect


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
