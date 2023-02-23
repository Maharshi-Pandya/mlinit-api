# this module is responsible for getting the 
# description and information of the dataset

import pandas as pd
import numpy as np

from utils import web

class Info:
    """
        information analysis:
        
        column names, null values, data-types,
        memory usage, and dataset size
    """
    def __init__(self, url: str):
        self.url = url
        self.df = None
        
    def _read_url(self):
        """
            create dataframe from the url
        """
        f = web.read_dataset_from_url(self.url)
        self.df = pd.read_csv(f)
        
    def perform_info(self):
        """
            perform info statistics
        """
        if self.df is None:
            self._read_url()
                      
        # TODO: what if the dataset is a pandas series?
        
        cols = list(self.df.columns)
        rows = self.df.shape[0]
        
        null = list(self.df.isnull().sum())
        dtypes = [str(d) for d in list(self.df.dtypes)]

        mem_use_mb = self.df.memory_usage(deep=True).sum() / 1000000
        
        result = {
            "columns": [],
            "shape": [0, 0],
            "memoryUsageMB": 0
        }
        
        for i, feat in enumerate(cols):
            feat_info = {
                "name": feat,
                "nullValuesCount": null[i],
                "dtype": dtypes[i]
            }
            result["columns"].append(feat_info)
        
        result["shape"][0], result["shape"][1] = rows, len(cols)
        result["memoryUsageMB"] = mem_use_mb
        return result
        