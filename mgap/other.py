# -*- coding: utf-8 -*-
import pandas as pd

#df = pd.read_csv("../data/TNPRC_sequence_data.csv", index_col=False)
#
#male_whole_genome_ids = list(df.query('sequence_type != "Whole Exome" & gender != "f"')['mgap_id'])
#
#
#male_wgs = df[df["mgap_id"].isin(male_whole_genome_ids)]
#male_wgs.to_csv("../data/TNPRC_males_wholegenome.csv", index=False)
#
#
## Save ids of wgs and male animals
#male_wgs['mgap_id'].to_csv(
#    "../data/tnprc_males_wholegenome.txt", header=False, index=False, sep=' ', mode='w')


#all_nprcs = pd.read_csv("../data/all_nprcs_metadata.csv", index_col=False)
#
#only_wgs = all_nprcs.query('sequence_type != "GBS" & sequence_type != "Whole Exome"')
#
#only_wgs.to_csv("../data/all_nprcs_wgs.csv", index=False)
#
## Save ids of wgs animals
#only_wgs['mgap_id'].to_csv(
#    "../data/wgs_ids.txt", header=False, index=False, sep=' ', mode='w')