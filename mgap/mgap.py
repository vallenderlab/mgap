# Accessing mGAP's labkey based api
# This script targets the client api version 0.4.0 and later
import sys
import os
from pathlib import Path

import labkey
from pandas.io.json import json_normalize


class MGap:

    def __init__(self, path=None):
        self.centers = ["CPRC", "CNPRC", "TNPRC", "NEPRC",
                        "YNPRC", "ONPRC", "WNPRC", "SNPRC"]
        
        self.path = self._set_path(path=path)

        self.server_context = self.login()

    def _create_file(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    def _set_path(self, path):
        if not path:
            path = str(Path.home())
            print("Path set to: %s" % path)
        elif not os.path.exists(path):
            raise FileNotFoundError("Path does not exist.")
        else:
            print("Path set to: %s" % path)
        return path

    def create_netrc(self, email, password):
        self._set_path()
        machine = "machine mgap.ohsu.edu\n"
        user_content = "login {}\npassword {}".format(email, password)
        file_str = machine + user_content
        if sys.platform == "linux":
            # create .netrc
            self._create_file(filename=".netrc", content=file_str)
        elif sys.platform == "win32":
            # create _netrc
            # The "home" path needs to be in the path variables on windows.
            self._create_file(filename="_netrc", content=file_str)
        else:
            print('%s not supported.' % sys.platform)
        
    def login(self, use_ssl=True):
        """Login to mgap."""
        machine = 'mgap.ohsu.edu'
        name = 'mGAP'
        server_context = labkey.utils.create_server_context(
            machine, name, use_ssl=use_ssl)
        return server_context

    def get_cohort_data(self, schema_name="study", query_name="demographics",
                        sort="mgapId"):
        cohort_data = labkey.query.select_rows(
            server_context=self.server_context,
            schema_name=schema_name,
            query_name=query_name,
            sort=sort
        )
        return cohort_data

    def get_sequence_data(self):
        sequence_data = labkey.query.select_rows(
            server_context=self.server_context,
            schema_name='mgap',
            query_name='sequenceDatasets',
            sort='mgapId'
        )
        return sequence_data

    def get_variant_data(self):
        variant_data = labkey.query.select_rows(
            server_context=self.server_context,
            schema_name='mgap',
            query_name='variantList',
            filter_array=[
                labkey.query.QueryFilter('releaseId/rowid', '3835', 'eq')
            ],
            sort='contig,position'
        )
        return variant_data

    def normalize_data(data, save=True, filename=None):
        """Turn the json output to a pandas dataframe."""
        df = json_normalize(data['rows'])
    
        if save:
            # Save the dataframe to a csv
            df.to_csv(filename, index=False)
        return df

server_context = MGap(path=r'C:\Users\shutchins2\Documents\test')
