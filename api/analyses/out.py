# this module is responsible for calculating the outliers
# using methods like z-score and quantiles

import pandas as pd
import numpy as np

from scipy import stats

# for reading the dataset
from utils import web


class Outliers:
    """
        calculate dataset outliers using zscore and quantiles
    """
    
    def __init__(self, url):
        self.url = url
        self.df = None
        
    def _read_url(self):
        """
            create dataframe from the url
        """
        f = web.read_dataset_from_url(self.url)
        self.df = pd.read_csv(f)
        
    def perform_out(self, method="zscore"):
        """
            perform outliers test using any method:
            
            - zscore
            - quantiles
        """
        if self.df is None:
            self._read_url()
            
        cols = self.df.shape[1]
        rows = self.df.shape[0]
        
        # get numeric features
        num_features = [self.df.select_dtypes(include=["number"]).count()][0].index
        num_features = list(num_features)
        feats_len = len(num_features)
            
        if method == "zscore":
            zouts = [0 for _ in range(feats_len)]
            
            for i, col in enumerate(num_features):
                abs_zscores = np.abs(stats.zscore(self.df[col], nan_policy="omit") < 3)
                zscores_col = self.df[abs_zscores][col]
                
                # difference is the outliers count
                num_outliers = self.df[col].shape[0] - zscores_col.shape[0]
                
                zouts[i] = num_outliers
            
            # json response
            result = {
                "columns": [],
                "shape": [rows, cols]
            }
            
            for i, feat in enumerate(num_features):
                feat_out = {
                    "name": feat,
                    "outliersZscore": zouts[i]
                }
                result["columns"].append(feat_out)

            return result