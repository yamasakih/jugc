# import os
# from typing import Any, List

# import pandas as pd
# from jug import bvalue
# from jug import execution_loop
from jug import TaskGenerator
# from jug.options import parse
# from rdkit import Chem, RDConfig
# from rdkit.Chem.rdchem import Mol

from jugc import calculate_descriptors

calculate_descriptors = TaskGenerator(calculate_descriptors)
print('test')
"""
input_file = os.path.join(RDConfig.RDDataDir, 'NCI', 'first_200.props.sdf')
supp = Chem.SDMolSupplier(input_file)
mols: List[Mol] = [mol for mol in supp]
descs = [calculate_descriptors(mol) for mol in mols]

argv: List[Any] = []
argv.insert(0, '/Users/yamasamkih/anaconda3/envs/dev_jugc/bin/jug')
argv.insert(1, 'execute')
argv.insert(2, 'subprocess.py')
print(argv)

options = parse()
execution_loop()
print(options)

df: pd.DataFrame = pd.concat(bvalue(descs))
df.to_csv('descs.csv', index=False)
"""
