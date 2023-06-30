import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")



from src.components.data_reading import reading_smiles_labels
from src.components.data_reading import reading_ppinteraction
from src.components.data_reading import reading_cancer_cell_lines


def filtering_1():

    ccle_attr, cell2ind, gene2ind, cell2exp = reading_cancer_cell_lines()
    pp_int = reading_ppinteraction()
    
    # If any genes are cell line ids, we will remove them
    cell_ids = cell2ind['Cell_lines'].unique()
    to_drop = []
    for i in range(len(gene2ind)):
        if(gene2ind.iloc[i]['Genes'] in cell_ids):
            to_drop.append(i)
    gene2ind = gene2ind.drop(to_drop, axis = 0)

    # Considering the Protein-Protein interaction data
    #   check and take intersection of gene_ids  
    p1p2 = set(np.concatenate((pp_int['Protein1'].unique(), 
                               pp_int['Protein1'].unique())))

    ## Check if any gene ids from deepsynergy dataset is missing in this p1p2
    common_gene_ids = []; 
    uncommon_gene_ids = [];
    for i in range(len(gene2ind)):
        if(gene2ind.iloc[i]['Gene_id'] in p1p2):
            common_gene_ids.append(gene2ind.iloc[i]['Gene_id'])
        else:
            uncommon_gene_ids.append(gene2ind.iloc[i]['Gene_id'])
    
    # Considering the ccle_attr (Cancer Cell Line Attribute data)
    #   Filtering out by removing gene ids note present in the gene2ind
    #   In other words, remove rows where id not present in common gene ids.
    old_shape = ccle_attr.shape
    to_drop = []
    for i in range(2, len(ccle_attr)):
        if(ccle_attr.iloc[i]['CellLine'] not in common_gene_ids):
            to_drop.append(i)
    ccle_attr = ccle_attr.drop(to_drop, axis = 0)

    # Considering the Protein-Protein Interaction dataset - pp_int
    #   Dropping uncommon genes from pp_int
    to_drop = set()
    for i in range(len(pp_int)):
        if(pp_int.iloc[i]['Protein1'] not in common_gene_ids):    to_drop.add(i)
        if(pp_int.iloc[i]['Protein2'] not in common_gene_ids):    to_drop.add(i)
    to_drop = list(to_drop)
    pp_int = pp_int.drop(to_drop, axis = 0)

    # Resetting the indexes for both ccle_attr and pp_int:
    ccle_attr = ccle_attr.reset_index().drop(['index'], axis = 1)
    pp_int = pp_int.reset_index().drop(['index'], axis = 1)

    # It was observed that the two above datasets still don't match
    # Thus we remove all extra genes from ccle_attr dataset
    genes_in_pp = list(set(np.concatenate((pp_int['Protein1'].unique(), 
                                           pp_int['Protein2'].unique()))))
    to_drop = []
    for i in range(2, len(ccle_attr)):
        if(ccle_attr.iloc[i]['CellLine'] not in genes_in_pp):
            to_drop.append(i)
    ccle_attr = ccle_attr.drop(to_drop, axis = 0)

    # Resetting the indexes for both ccle_attr and pp_int:
    ccle_attr = ccle_attr.reset_index().drop(['index'], axis = 1)
    pp_int = pp_int.reset_index().drop(['index'], axis = 1)

    # Saving these two dataset
    ccle_attr.to_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Processed\ccle_attr_updated.csv", index=False)
    pp_int.to_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Processed\pp_int_updated.csv", index=False)

    return ccle_attr, pp_int