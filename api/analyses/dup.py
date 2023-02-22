# this module is responsible for performing
# duplicates analysis on the dataset

import pandas as pd
import numpy as np


class Duplicate:
    """
        find the number of duplicate rows
        in the dataset
    """
    def __init__(self, url: str):
        self.url = url
        self.df = None
        
    def _read_url(self):
        """
            create dataframe from the url
        """
        self.df = pd.read_csv(self.url)
        
    def perform_dup(self):
        """
            perform duplicates analysis
        """
        if self.df is None:
            self._read_url()
        
        rows = self.df.shape[0]
        cols = self.df.shape[1]
        
        ndf = self.df[self.df.duplicated() == True]
        dup_rows = ndf.shape[0]
        dup_cols = ndf.shape[1]
        
        difference = rows - dup_rows
        result = {
            "shapeBefore": [rows, cols],
            "duplicateRows": dup_rows,
            "difference": difference,
            "shapeAfter": [dup_rows, dup_cols]
        }
        
        return result
        