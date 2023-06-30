import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")



# --------------------------------
# Reading the Smiles & Labels Data
# --------------------------------

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
# ----------------------------
smiles_labels_final.to_csv(r"G:\My Drive\Study\Project-cancer-drug-synergy-prediction\Data\Processed\smiles_labels_final.csv", index=False)