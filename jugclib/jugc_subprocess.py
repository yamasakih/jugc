import argparse
from typing import List

from jug import bvalue
from jug import TaskGenerator
import pandas as pd
from rdkit import Chem
from rdkit.Chem.rdchem import Mol

from jugclib import calculate_descriptors

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description='Calculate descriptors.')
parser.add_argument('-i', '--input', required=True, type=str, help='Input SDF')
parser.add_argument('-o',
                    '--output',
                    required=True,
                    type=str,
                    help='Output csv')


def main() -> None:
    args = parser.parse_args()

    calculate_descriptors = TaskGenerator(calculate_descriptors)

    input_file = args.input
    output_file = args.output

    supp = Chem.SDMolSupplier(input_file)
    mols: List[Mol] = [mol for mol in supp]
    tasks = [calculate_descriptors(mol) for mol in mols]

    descs: pd.DataFrame = pd.concat(bvalue(tasks))
    descs.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()
