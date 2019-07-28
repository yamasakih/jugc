import os
from typing import List

from jug import bvalue
from jug import TaskGenerator
import pandas as pd
from rdkit import Chem
from rdkit import RDConfig
from rdkit.Chem.rdchem import Mol

from jugc import calculate_descriptors

calculate_descriptors = TaskGenerator(calculate_descriptors)

input_file = os.path.join(RDConfig.RDDataDir, 'NCI', 'first_200.props.sdf')
supp = Chem.SDMolSupplier(input_file)
mols: List[Mol] = [mol for mol in supp]
descs = [calculate_descriptors(mol) for mol in mols]

df: pd.DataFrame = pd.concat(bvalue(descs))
df.to_csv('descs.csv', index=False)
