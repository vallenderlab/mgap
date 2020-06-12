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

x = 'm02205,m02206,m02207,m02208,m02209,m02210,m02211,m02212,m02213,m02214,m02215,m02216,m02217,m02193,m02194,m02166,m02167,m02168,m02169,m02170,m02171,m02172,m02173,m02174,m02175,m03585,m03586,m03587,m03588,m03589,m03590,m03591,m03592,m03593,m03594,m03595,m03596,m03597,m03598,m03599,m03600,m03601,m03602,m03603,m03604,m03605,m03606,m00834,m00835,m00836,m00837,m00838,m00839,m00840,m00841,m00842,m00843,m00844,m00845,m00846,m00847,m00848,m00849,m00850,m00851,m00852,m00853,m00854,m00855,m00856,m00857,m00858,m00859,m00860,m00861,m00862,m00863,m00864,m00865,m00866,m00867,m00868,m00869,m00870,m00871,m00872,m00873,m00874,m00875,m00876,m00877,m02176,m02177,m02178,m02179,m02180,m02181,m02182,m02183,m02184,m02185,m02186,m02187,m02188,m02189,m02190,m02191,m02192,m03541,m03542,m03543,m03544,m03545,m03546,m03547,m03548,m03549,m03550,m03551,m03552,m03553,m03554,m03555,m03556,m03557,m03558,m03559,m03560,m03561,m03562,m03563,m03564,m03565,m03566,m03567,m03568,m03569,m03570,m03571,m03572,m03573,m03574,m03575,m03576,m03577,m03578,m03579,m03580,m03581,m03582,m03583,m03584,m00327,m00328,m00329,m00330,m00331,m00332,m00333,m00334,m00335,m00336,m00337,m00338,m00345,m00356,m00357,m00359,m00360,m00365,m00366,m00368,m00369,m00372,m00378,m00381,m00385,m00389,m00398,m00404,m00411,m00412,m00414,m00416,m00417,m00424,m00428,m00431,m00432,m00433,m00434,m00435,m00436,m00437,m00438,m00439,m00440,m00441,m00442,m00443,m00444,m00445,m00446,m00447,m00448,m00449,m00450,m00451,m00452,m00453,m00454,m00455,m00456,m00457,m00458,m00459,m00460,m00461,m00462,m00463,m00464,m00465,m00466,m00467,m00468,m00470,m00471,m00472,m00473,m00474,m00475,m00481,m00482,m00483,m00484,m00485,m00486,m00487,m00488,m00535,m00569,m00570,m00571,m00572,m00573,m00574,m00575,m00576,m00577,m00578,m00579,m00580,m00581,m00582,m00583,m00584,m00585,m00586,m00587,m00588,m00589,m00590,m00591,m00592,m00593,m00594,m00595,m00596,m00597,m00598,m00599,m00600,m00601,m00602,m00603,m00604,m00605,m00606,m00607,m00608,m00609,m00610,m00611,m00612,m00613,m00614,m00629,m00638,m00769,m00780,m00789,m00791,m00801,m00806,m00807,m00808,m00809,m00810,m00811,m00812,m00813,m00814,m00815,m00816,m00817,m00818,m00819,m00820,m00821,m00822,m00823,m00824,m00825,m00826,m00827,m00828,m00829,m00830,m00831,m00832,m00833,m00878,m00879,m00880,m00881,m00882,m00883,m00884,m00935,m00937,m00956,m00963,m00965,m00980,m01009,m01026,m01040,m01048,m02219,m02220,m02221,m02222,m02224,m02225,m02227,m02229,m02230,m02234,m02235,m02237,m02238,m02239,m02240,m02241,m02242,m02243,m02244,m02245,m02246,m02248,m02321,m02464,m03607,m03608,m03609,m03610,m03611,m03612,m03613,m03614,m03616,m03617,m03618,m03619,m03620,m03621,m03622,m03623,m03624,m00001,m00002,m00003,m00006,m00007,m00008,m00009,m00010,m00012,m00016,m00019,m00020,m00021,m00022,m00023,m00024,m00025,m00026,m00027,m00028,m00029,m00030,m00031,m00032,m00033,m00034,m00035,m00036,m00037,m00038,m00039,m00040,m00041,m00042,m00043,m00044,m00045,m00046,m00047,m00048,m00049,m00050,m00051,m00052,m00053,m00054,m00055,m00056,m00057,m00058,m00059,m00060,m00061,m00071,m00073,m00082,m00084,m00087,m00099,m00101,m00116,m00117,m00119,m00123,m00132,m00133,m00134,m00135,m00136,m00137,m00138,m00139,m00140,m00141,m00142,m00143,m00144,m00145,m00146,m00147,m00148,m00149,m00150,m00151,m00152,m00153,m00154,m00160,m00162,m00213,m00236,m00246,m00262,m00277,m00292,m00293,m00295,m00296,m00297,m00300,m00302,m00308,m00309,m00310,m00311,m00312,m00313,m00314,m00315,m00316,m00317,m00318,m00319,m00320,m00321,m00322,m00323,m00324,m00325,m00326,m02195,m02196,m02197,m02198,m02199,m02200,m02201,m02202,m02203,m02204,m03630,m03631,m03632,m03633,m03634,m03635,m03636,m03637,m03638,m03639,m03640,m03641,m03642,m03643,m03644,m03645,m03646,m03647,m03648,m03649,m03650,m03651,m03652,m03653,m03654,m03655,m03656,m03657,m03658,m03659,m03660,m03661,m03662,m03663,m03664,m03665,m03666,m03667,m03668,m03669,m03670,m03671,m03672,m03673,m03674,m03675,m03676,m03677,m03678,m03679,m03680,m03681,m03682,m03683,m03684,m03685,m03686,m03687,m03688,m03689,m03690,m03691,m03692,m03693,m03694,m03695,m03696,m03697,m03698'
ids = x.split(',')

all_nprcs = pd.read_csv("../data/all_nprcs_metadata.csv", index_col=False)

whole_seq_data = pd.read_csv("../data/mgap_sequence_datasets.csv", index_col=False)

data = whole_seq_data[whole_seq_data["mgapId"].isin(ids)]

data_wgs = data.query('sequenceType != "GBS" & sequenceType != "Whole Exome"')

data_gbs = data.query('sequenceType == "GBS"')

data_gbs = data_gbs[data_gbs["mgapId"].isin(ids)]

data_ex = data.query('sequenceType == "Whole Exome"')

data_ex = data_ex[data_ex["mgapId"].isin(ids)]


not_in_datawgs = list(set(ids).difference(list(data_wgs.mgapId)))

#data_wgs.to_csv("../data/only_exome_vcf.csv", index=False)

ids_not_in = whole_seq_data[whole_seq_data["mgapId"].isin(not_in_datawgs)]

whole_seq_data = pd.read_csv("../data/mgap_sequence_datasets.csv", index_col=False)

mgap_demos = pd.read_csv("../data/mgap_demographics.csv", index_col=False)

ids_not_in2 = mgap_demos[mgap_demos["Id"].isin(not_in_datawgs)]

ids_not_in3 = all_nprcs[all_nprcs["mgap_id"].isin(not_in_datawgs)]
ids_not_in3 = ids_not_in3.query('sequence_type == "GBS"')

data_wgs = data_wgs.rename(columns={"mgapId/gender": "gender",
                              "mgapId/geographic_origin": "geographic_origin",
                              "mgapId/species": "species",
                              "totalReads": "total_reads",
                              "sraAccession": "sra_accession",
                              "sequenceType": "sequence_type",
                              "mgapId": "mgap_id"})

all_nprcs_wgs = all_nprcs.query('sequence_type != "GBS" & sequence_type != "Whole Exome"')
wgs = all_nprcs_wgs[all_nprcs_wgs["mgap_id"].isin(ids)]

not_found = ['m03613',
             'm03610',
             'm03614',
 'm03611',
 'm03624',
 'm03612',
 'm03621',
 'm03623',
 'm03617',
 'm03616',
 'm03607',
 'm03619',
 'm03609',
 'm03620',
 'm03622',
 'm03608',
 'm03618']

d = mgap_demos[mgap_demos["Id"].isin(not_found)]
e = whole_seq_data[whole_seq_data["mgapId"].isin(not_found)]
f = all_nprcs[all_nprcs["mgap_id"].isin(not_found)]

# Create empty dataframe
newdf = pd.DataFrame(index=None, columns= list(wgs.columns))
newdf.mgap_id = not_found


wgs.to_csv("../data/all_nprc_wgs_metadata.csv", index=False)
newdf.to_csv("../data/no_seq_data.csv", index=False)

# Save ids of wgs animals
with open("../data/gbs_or_exome_ids.txt", 'w') as filehandle:
    filehandle.writelines("%s\n" % id for id in list(set(ids_not_in3.mgap_id)))
    
with open("../data/no_seq_data_ids.txt", 'w') as filehandle:
    filehandle.writelines("%s\n" % id for id in not_found)