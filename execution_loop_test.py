import os
from typing import List

import pandas as pd
from jug import bvalue
from jug import TaskGenerator
from jug.jug import execution_loop
from jug.jug import init
from jug.options import parse
from jug.task import value
from rdkit import Chem, RDConfig
from rdkit.Chem.rdchem import Mol

from jugc import calculate_descriptors

calculate_descriptors = TaskGenerator(calculate_descriptors)

# input_file = os.path.join(RDConfig.RDDataDir, 'NCI', 'first_200.props.sdf')
input_file = 'logSdataset1290_2d.sdf'
supp = Chem.SDMolSupplier(input_file)
mols: List[Mol] = [mol for mol in supp]
tasks = [calculate_descriptors(mol) for mol in mols]

argv: List[str] = ['execute', '--will-cite', 'jugc/subprocess.py']
# argv.insert(0, '/Users/yamasamkih/anaconda3/envs/dev_jugc/bin/jug')
# argv.insert(0, 'execute')
print(argv)

options = parse(args=argv)
print(options.__dict__)

store, space = init(options.jugfile, 'dict_store')

for _ in range(20):
    execution_loop(tasks, options)

print(store)
# print(store.store)
print(len(store.store))

# store.store.
descs: pd.DataFrame = pd.concat([store.load(key) for key in store.list()])
descs.reset_index(drop=True, inplace=True)
print(descs.head())
descs.to_csv('descs.csv', index=False)
