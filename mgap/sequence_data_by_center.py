# -*- coding: utf-8 -*-
import pandas as pd

# List of primate centers
nprcs = ["CPRC", "CNPRC", "TNPRC", "NEPRC", "YNPRC", "ONPRC", "WNPRC",
         "SNPRC"]

# Sample file format
sample_files = "{}_sample_ids.txt"

# Sequence dataset for mgap
seq_data = pd.read_csv("../data/mgap_sequence_datasets.csv")

# Demographic data for mgap
mgap_demo = pd.read_csv("../data/mgap_demographics.csv", index_col=False)

# Create empty lists
centers = []
ids = []
dfs = []
only_exomes = []
ids_no_data = []

# Dictionary of new column names
new_cols = {"mgapId/gender": "gender",
                                  "mgapId/geographic_origin": "geographic_origin",
                                  "mgapId/species": "species",
                                  "totalReads": "total_reads",
                                  "sraAccession": "sra_accession",
                                  "sequenceType": "sequence_type",
                                  "mgapId": "mgap_id"}

# A loop to extract sequence data for each center.
for center in nprcs:
    with open("../data/%s" % sample_files.format(center), 'r') as f:
        x = f.read().splitlines()
    newdf = seq_data[seq_data['mgapId'].isin(x)]
    newdf = newdf.rename(columns=new_cols)
    del newdf["rowid"]

    no_data_ids = list(set(x).difference(list(newdf.mgap_id)))
    demo = mgap_demo[mgap_demo['Id'].isin(no_data_ids)]
    demo = demo.sort_values(by=['Id'])
    # Create empty dataframe
    no_data_df =  pd.DataFrame(index=None, columns= list(newdf.columns))
    no_data_df.mgap_id = no_data_ids
    no_data_df = no_data_df.sort_values(by=['mgap_id'])
    # if no_data_ids > 0:
    #     # Add data by id.
    #     for id in no_data_ids:
    #         no_data_df.gender = demo.gender
    #         no_data_df.species = demo.species
    #         no_data_df.geographic_origin = demo.geographic_origin
    
    ids_no_data.extend(no_data_ids)
    ids.extend(x)
    new_df = pd.concat([newdf, no_data_df], axis=0)
    centers.extend(str.split(len(new_df['mgap_id']) * (center + " ")))
    dfs.append(new_df)
    # Save center by center dataframe
    new_df.to_csv("../data/%s_sequence_data.csv" % center, index=False)

# Prepare
all_nprcs = pd.concat(dfs)
all_nprcs["primate_center"] = centers
columns = ['mgap_id',
           'primate_center',
           'gender',
           'geographic_origin',
           'species',
           'sequence_type',
           'sra_accession',
           'total_reads']
all_nprcs = all_nprcs[columns]
all_nprcs = all_nprcs.sort_values('primate_center')
all_nprcs.to_csv("../data/all_nprcs_metadata.csv", index=False)

#no_exome_ids = all_nprcs.query('sequence_type != "Whole Exome"')['mgap_id']
#no_ex_list = list(no_exome_ids)
#only_exomes = all_nprcs[~all_nprcs["mgap_id"].isin(no_ex_list)]
#only_exomes.to_csv("data/all_nprcs_only_exome_available.csv", index=False)
#
## Save ids of exome only animals
#only_exomes['mgap_id'].to_csv(
#    "data/only_exome_ids.txt", header=False, index=False, sep=' ', mode='w')


wgs = all_nprcs.query('sequence_type != "GBS" & sequence_type != "Whole Exome" & sequence_type == "Whole Genome: Deep Coverage"')
wgs.sort_values(by=['mgap_id'], inplace=True)
wgs.to_csv("../data/all_nprcs_wgs.csv", index=False)

wgs_ind = wgs.query('geographic_origin == "India" or geographic_origin == "INDIA"')
wgs_ind.sort_values(by=['mgap_id'], inplace=True)
wgs_ind.to_csv("../data/all_nprcs_wgs_india.csv", index=False)

# Save ids of wgs animals
with open("../data/wgs_india_ids.txt", 'w') as filehandle:
    filehandle.writelines("%s\n" % id for id in list(set(wgs_ind.mgap_id)))