# Accessing mGAP's labkey based api
# This script targets the client api version 0.4.0 and later
import labkey
from pandas.io.json import json_normalize

server_context = labkey.utils.create_server_context(
    'mgap.ohsu.edu', 'mGAP', use_ssl=True)


# Getting cohort data
cohort_data = labkey.query.select_rows(
    server_context=server_context,
    schema_name='study',
    query_name='demographics',  # or 'sequenceDatasets',
    sort='mgapId'
)

# Getting sequence datasets
sequence_data = labkey.query.select_rows(
    server_context=server_context,
    schema_name='mgap',
    query_name='sequenceDatasets',  # or 'sequenceDatasets',
    sort='mgapId'
)

# Turn the json output of the labkey query to a pandas dataframe
df = json_normalize(cohort_data['rows'])

# Save the dataframe to a csv
df.to_csv('mgap_demographics.csv', index=False)

###############################################################################
########## The below are other examples of accessing the mGAP api.#############
###############################################################################

# Getting phenotype information for the latest genome release
my_results = labkey.query.select_rows(
    server_context=server_context,
    schema_name='mgap',
    query_name='phenotypes',
    filter_array=[
        labkey.query.QueryFilter('releaseId/rowid', '3835', 'eq')
    ],
    sort='releaseId/rowId,omim_phenotype'
)

# Getting variant information for a specific phenotype/omim id
my_results = labkey.query.select_rows(
    server_context=server_context,
    schema_name='mgap',
    query_name='variantList',
    filter_array=[
        labkey.query.QueryFilter('omim_phenotype', '264300', 'contains'),
        labkey.query.QueryFilter('releaseId/rowid', '3835', 'eq')
    ],
    sort='contig,position'
)

# View all variants
variant_data = labkey.query.select_rows(
    server_context=server_context,
    schema_name='mgap',
    query_name='variantList',
    filter_array=[
        labkey.query.QueryFilter('releaseId/rowid', '3835', 'eq')
    ],
    sort='contig,position'
)

# Turn the json output of the labkey query to a pandas dataframe
df = json_normalize(variant_data['rows'])

# Save the dataframe to a csv
df.to_csv('all_variants_mgap.csv', index=False)
