# -*- coding: utf-8 -*-
import pandas as pd

nprcs = ["CPRC", "CNPRC", "TNPRC", "NEPRC", "YNPRC", "ONPRC", "WNPRC", 
           "SNPRC"]

sample_files = "{}_sample_ids.txt"

seq_data = pd.read_csv("data/mgap_sequence_datasets.csv")

centers = []
ids = []
dfs = []
only_exomes = []

for center in nprcs:
    with open("data/%s" % sample_files.format(center), 'r') as f:
        x = f.read().splitlines()
    newdf = seq_data[seq_data['mgapId'].isin(x)]
    newdf = newdf.rename(columns={"mgapId/gender": "gender", 
                              "mgapId/geographic_origin": "geographic_origin",
                              "mgapId/species": "species",
                              "totalReads": "total_reads",
                              "sraAccession": "sra_accession",
                              "sequenceType": "sequence_type",
                              "mgapId": "mgap_id"})
    del newdf["rowid"]
    # Save center by center dataframe
    newdf.to_csv("data/%s_sequence_data.csv" % center, index=False)
    ids.extend(x)
    centers.extend(str.split(len(newdf['mgap_id']) * (center + " ")))
    dfs.append(newdf)

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
all_nprcs.to_csv("data/all_nprcs_metadata.csv", index=False)

no_exome_ids = all_nprcs.query('sequence_type != "Whole Exome"')['mgap_id']
no_ex_list = list(no_exome_ids)
only_exomes = all_nprcs[~all_nprcs["mgap_id"].isin(no_ex_list)]
only_exomes.to_csv("data/all_nprcs_only_exome_available.csv", index=False)

# Save ids of exome only animals
only_exomes['mgap_id'].to_csv("data/only_exome_ids.txt", header=False, index=False, sep=' ', mode='w')