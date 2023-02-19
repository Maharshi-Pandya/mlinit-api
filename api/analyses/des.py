# this module is responsible to get the summary statistics
# of the given dataset

import pandas as pd
import numpy as np


class Describe:
    """
        description analysis:
        
        calculate the mean, standard deviation, and
        other statistical measures
        
        in short, describe the data
    """
    def __init__(self, url: str):
        self.url = url
        self.df = None
        
    def _read_url(self):
        """
            create the dataframe from url
        """
        self.df = pd.read_csv(self.url)
    
    def perform_des(self):
        """
            describe the data
        """
        if self.df is None:
            self._read_url()
            
        # TODO: what if the dataset is a pandas series?
        
        rows = self.df.shape[0]
        cols = list(self.df.columns)
        
        summ = self.df.describe(include="all")
        summ = summ.to_dict()
        
        result = {
            "columns": [],
            "shape": [rows, len(cols)]
        }

        for feat in cols:
            feat_summ = {
                "name": feat,
                "summary": summ[feat]
            }
            result["columns"].append(feat_summ)
            
        return result