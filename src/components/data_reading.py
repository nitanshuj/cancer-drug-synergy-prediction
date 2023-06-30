import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")




def reading_smiles_labels():

    """
    # Reading the Smiles & Labels Data
    """

    smiles = pd.read_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Raw\smiles.csv",header=None)
    smiles.columns = ["drug_name", "drug_smiles"]

    labels = pd.read_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Raw\labels.csv")
    labels = labels.rename(columns={"Unnamed: 0":"information"})

    smiles_labels_final = labels[['drug_a_name', 'drug_b_name', 'cell_line', 'fold', 'synergy']]

    # Adding smiles structure for Drug A
    smiles_labels_final = pd.merge(smiles_labels_final, smiles, left_on='drug_a_name', right_on='drug_name', how='left')
    smiles_labels_final.rename(columns={"drug_smiles":"drug_a_structure"}, inplace=True)

    # Adding smiles structure for Drug B
    smiles_labels_final = pd.merge(smiles_labels_final, smiles, left_on='drug_b_name', right_on='drug_name', how='left')
    smiles_labels_final.rename(columns={"drug_smiles":"drug_b_structure"}, inplace=True)
    smiles_labels_final.drop(["drug_name_x", "drug_name_y"], axis=1, inplace=True)

    # Converting Final data to csv
    smiles_labels_final.to_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Processed\smiles_labels_final.csv", index=False)
    
    return smiles_labels_final


def reading_cancer_cell_lines():
    # Read attribute matrix
    ccle_attr = pd.read_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Raw\gene_attribute_matrix.txt.gz",sep='\t')
    
    # Extracting cell data
    cell2ind = pd.DataFrame(columns=['index', 'Cell_lines'])
    cell2ind['Cell_lines'] = list(ccle_attr.columns[3:])
    cell2ind['index'] = list(cell2ind.index)
    
    # Extracting gene data
    gene2ind = pd.DataFrame(columns=['index', 'Genes', 'Gene_id'])
    gene2ind['Genes'] = list(ccle_attr['#'].values[2:])
    gene2ind['index'] = list(gene2ind.index)
    gene2ind['Gene_id'] = list(ccle_attr['CellLine'].values[2:])
    
    # Getting the Cell Expressions    
    cell2exp = pd.DataFrame(columns=['expression'])
    l = []
    for cells_ind in range(len(cell2ind['Cell_lines'])):
        l.append(list(ccle_attr[cell2ind['Cell_lines'].iloc[cells_ind]].values[2:]))
    cell2exp['expression'] = l


    return ccle_attr, cell2ind, gene2ind, cell2exp


def reading_ppinteraction():
    pp_int = pp_int = pd.read_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Raw\PP-Pathways_ppi.csv.gz",header=None)
    pp_int.columns = ['Protein1', 'Protein2']
    return pp_int



