from typing import List
from typing import Optional

import numpy as np
import pandas as pd
from rdkit.Chem import Descriptors
from rdkit.Chem.rdchem import Mol
from rdkit.ML.Descriptors import MoleculeDescriptors

__version__ = '0.1.0b0'

__all__ = [
    'calculate_descriptors',
]


def calculate_descriptors(mol: Mol,
                          names: Optional[List[str]] = None,
                          ipc_avg: bool = True) -> pd.DataFrame:
    """
    Calculate the descriptors for input molecule. If Mol is None, all NaN
    values are returned.

    Parameters
    ----------
    mol : rdKit.Chem.rdchem.Mol
        Input molecule

    names : list, default None
        List of descriptors to calculate. By default, all descriptors included
        in RDKit rdkit.Chem.Descriptors are calculated. There are 200
        descriptors in version 2019.03.3.

    ipc_avg : bool, default True
        If = True, prevents the Ipc descriptor value from becoming very large.
        See https://github.com/rdkit/rdkit/issues/1527 for details.

    Returns
    -------
    pandas.DataFrame
        Return calculated descriptors as pandas.DataFrame
    """
    if names is None:
        names = [d[0] for d in Descriptors._descList]
    if mol is not None:
        calc = MoleculeDescriptors.MolecularDescriptorCalculator(names)
        descs = calc.CalcDescriptors(mol)
    else:
        descs = np.repeat(np.nan, len(names))
    descs = pd.DataFrame(descs, index=names).T
    if 'Ipc' in names and ipc_avg:
        descs['Ipc'] = Descriptors.Ipc(mol, avg=True)
    return descs
