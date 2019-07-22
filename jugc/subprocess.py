import os
from typing import List
from typing import Union

from jug import barrier, TaskGenerator, value
import pandas as pd
from rdkit import Chem
from rdkit import RDConfig
from rdkit.Chem.rdchem import Mol

from jugc import calculate_descriptors

calculate_descriptors = TaskGenerator(calculate_descriptors)

input_file = os.path.join(RDConfig.RDDataDir, 'NCI', 'first_200.props.sdf')
supp = Chem.SDMolSupplier(input_file)
mols: List[Mol] = [mol for mol in supp]
descs: Union[List, pd.DataFrame] = [calculate_descriptors(mol) for mol in mols]

barrier()

descs = pd.concat(value(descs))
descs.to_csv('descs.csv', index=False)
