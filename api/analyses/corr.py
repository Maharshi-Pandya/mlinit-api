# this module is responsible to calculate the correlation
# matrix between all the features

import plotly.express as px
import plotly.io as pio
import pandas as pd
import json

from utils import web

class Correlation:
    """
        calculate and plot the correlation matrix
    """
    def __init__(self, url):
        self.url = url
        self.df = None
        
    def _read_url(self):
        """
            create dataframe from url
        """
        f = web.read_dataset_from_url(self.url)
        self.df = pd.read_csv(f)
        
    def perform_corr(self):
        """
            perform the calculation
        """
        if self.df is None:
            self._read_url()
            
        rows = self.df.shape[0]
        cols = self.df.shape[1]
        
        corr_mat = self.df.corr(numeric_only=True)
        fig = px.imshow(corr_mat, text_auto=True,
        aspect="auto", template="ggplot2", title="correlation matrix")
        
        # load to dict
        result = json.loads(pio.to_json(fig))
        response = {
            "plotObject": result,
            "shape": [rows, cols]
        }
        
        return response
        