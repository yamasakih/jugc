from typing import Any
import pandas as pd
from rdkit.Chem import Descriptors
from rdkit.Chem.rdchem import Mol
from rdkit.ML.Descriptors import MoleculeDescriptors

__version__ = '0.1.0'

__all__ = [
    'calculate_descriptors',
]


def calculate_descriptors(mol: Mol, names: Any = None, ipc_avg: bool = True):
    if names is None:
        names = [d[0] for d in Descriptors._descList]
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(names)
    descs = calc.CalcDescriptors(mol)
    descs = pd.DataFrame(descs, index=names).T
    if 'Ipc' in names and ipc_avg:
        descs['Ipc'] = Descriptors.Ipc(mol, avg=True)
    return descs
