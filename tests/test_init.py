import pkg_resources

import numpy as np
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
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = list(descs.columns)
    expect = ['MolWt']
    assert actual == expect

    actual = descs.at[0, 'MolWt']
    expect = 78.114
    assert pytest.approx(actual) == expect

    descs = calculate_descriptors(mol, names=None)

    actual = descs
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = descs.shape[1]
    expect = 200
    assert actual == expect

    actual = list(descs.columns)
    expect = [
        'MaxEStateIndex', 'MinEStateIndex', 'MaxAbsEStateIndex',
        'MinAbsEStateIndex', 'qed', 'MolWt', 'HeavyAtomMolWt', 'ExactMolWt',
        'NumValenceElectrons', 'NumRadicalElectrons', 'MaxPartialCharge',
        'MinPartialCharge', 'MaxAbsPartialCharge', 'MinAbsPartialCharge',
        'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'BalabanJ',
        'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n',
        'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'HallKierAlpha', 'Ipc',
        'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'PEOE_VSA1', 'PEOE_VSA10',
        'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2',
        'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7',
        'PEOE_VSA8', 'PEOE_VSA9', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2',
        'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA8',
        'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12',
        'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6',
        'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'EState_VSA1',
        'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3',
        'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7',
        'EState_VSA8', 'EState_VSA9', 'VSA_EState1', 'VSA_EState10',
        'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5',
        'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9',
        'FractionCSP3', 'HeavyAtomCount', 'NHOHCount', 'NOCount',
        'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles',
        'NumAliphaticRings', 'NumAromaticCarbocycles',
        'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors',
        'NumHDonors', 'NumHeteroatoms', 'NumRotatableBonds',
        'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles',
        'NumSaturatedRings', 'RingCount', 'MolLogP', 'MolMR', 'fr_Al_COO',
        'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N',
        'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO',
        'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2',
        'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole',
        'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate', 'fr_alkyl_halide',
        'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline',
        'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene',
        'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine',
        'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido',
        'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 'fr_imide',
        'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss',
        'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile',
        'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso',
        'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol',
        'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester',
        'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd',
        'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone',
        'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan',
        'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea'
    ]
    assert actual == expect

    actual = descs.at[0, 'fr_urea']
    expect = 0
    assert pytest.approx(actual) == expect

    mol = None

    descs = calculate_descriptors(mol, names=['MolWt'])

    actual = descs
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = list(descs.columns)
    expect = ['MolWt']
    assert actual == expect

    actual = descs.at[0, 'MolWt']
    assert np.isnan(actual)

    mol = MolFromSmiles('C1=CC(=CC=C1NC(C)=O)O')

    descs = calculate_descriptors(mol, names=['MolWt'])

    actual = descs
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = list(descs.columns)
    expect = ['MolWt']
    assert actual == expect

    actual = descs.at[0, 'MolWt']
    expect = 151.165
    assert pytest.approx(actual, 0.0001) == expect

    descs = calculate_descriptors(mol, names=['MolWt', 'HeavyAtomCount'])

    actual = descs
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = descs.shape[0]
    expect = 1
    assert actual == expect

    actual = descs.shape[1]
    expect = 2
    assert actual == expect

    actual = list(descs.columns)
    expect = ['MolWt', 'HeavyAtomCount']
    assert actual == expect

    actual = descs.at[0, 'MolWt']
    expect = 151.165
    assert pytest.approx(actual, 0.0001) == expect

    actual = descs.at[0, 'HeavyAtomCount']
    expect = 11
    assert actual == expect

    descs = calculate_descriptors(mol)

    actual = descs
    expect = pd.DataFrame
    assert isinstance(actual, expect)

    actual = descs.shape[1]
    expect = 200
    assert actual == expect

    actual = list(descs.columns)
    expect = [
        'MaxEStateIndex', 'MinEStateIndex', 'MaxAbsEStateIndex',
        'MinAbsEStateIndex', 'qed', 'MolWt', 'HeavyAtomMolWt', 'ExactMolWt',
        'NumValenceElectrons', 'NumRadicalElectrons', 'MaxPartialCharge',
        'MinPartialCharge', 'MaxAbsPartialCharge', 'MinAbsPartialCharge',
        'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'BalabanJ',
        'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n',
        'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'HallKierAlpha', 'Ipc',
        'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'PEOE_VSA1', 'PEOE_VSA10',
        'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2',
        'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7',
        'PEOE_VSA8', 'PEOE_VSA9', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2',
        'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA8',
        'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12',
        'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6',
        'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'EState_VSA1',
        'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3',
        'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7',
        'EState_VSA8', 'EState_VSA9', 'VSA_EState1', 'VSA_EState10',
        'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5',
        'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9',
        'FractionCSP3', 'HeavyAtomCount', 'NHOHCount', 'NOCount',
        'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles',
        'NumAliphaticRings', 'NumAromaticCarbocycles',
        'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors',
        'NumHDonors', 'NumHeteroatoms', 'NumRotatableBonds',
        'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles',
        'NumSaturatedRings', 'RingCount', 'MolLogP', 'MolMR', 'fr_Al_COO',
        'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N',
        'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO',
        'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2',
        'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole',
        'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate', 'fr_alkyl_halide',
        'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline',
        'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene',
        'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine',
        'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido',
        'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 'fr_imide',
        'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss',
        'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile',
        'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso',
        'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol',
        'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester',
        'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd',
        'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone',
        'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan',
        'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea'
    ]
    assert actual == expect

    actual = descs.at[0, 'NumAromaticRings']
    expect = 1
    assert pytest.approx(actual) == expect


def test_ipc() -> None:
    mol = MolFromSmiles('CCCCCCCCCC')
    descs = calculate_descriptors(mol, names=['Ipc'])

    actual = list(descs.columns)
    expect = ['Ipc']
    assert actual == expect

    actual = descs.at[0, 'Ipc']
    expect = 1.9671544  # type: ignore
    assert pytest.approx(actual) == expect

    descs = calculate_descriptors(mol, names=['Ipc'], ipc_avg=False)

    actual = list(descs.columns)
    expect = ['Ipc']
    assert actual == expect

    actual = descs.at[0, 'Ipc']
    expect = 175.07674799  # type: ignore
    assert pytest.approx(actual) == expect

    mol = MolFromSmiles('CCCCCCCCCCCCCCCCCCCCCCCCC')
    descs = calculate_descriptors(mol, names=['Ipc'], ipc_avg=True)

    actual = list(descs.columns)
    expect = ['Ipc']
    assert actual == expect

    actual = descs.at[0, 'Ipc']
    expect = 2.628133523535876  # type: ignore
    assert pytest.approx(actual) == expect

    descs = calculate_descriptors(mol, names=['Ipc'], ipc_avg=False)

    actual = list(descs.columns)
    expect = ['Ipc']
    assert actual == expect

    actual = descs.at[0, 'Ipc']
    expect = 319037.012823  # type: ignore
    assert pytest.approx(actual) == expect


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
