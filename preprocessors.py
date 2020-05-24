import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, features=None):
        if not isinstance(features, list):
            self.features = [features]
        else:
            self.features = features

    def fit(self, X, y=None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self
    
    # Helper function to get mean floor range
    def split_mean(self, x):
        split_list = x.split(' TO ')
        mean = (float(split_list[0])+float(split_list[1]))/2
        return mean
    
    def transform(self, X, y=None):
        for feature in self.features:
            if feature == 'flat_type':
                # Mapping ordinal categories to their respective values
                flat_type_map = {
                    'EXECUTIVE': 7,
                    'MULTI-GENERATION': 6,
                    '5 ROOM': 5,
                    '4 ROOM': 4,
                    '3 ROOM': 3,
                    '2 ROOM': 2,
                    '1 ROOM': 1
                }
                X['flat_type_mapped'] = X[feature].map(lambda x: flat_type_map[x])
            
            elif feature == 'storey_range':
                X['floor_mean'] = X[feature].apply(lambda x: self.split_mean(x))
            
            return X

class TemporalEncoder(BaseEstimator, TransformerMixin):
    
    def __init__(self, feature=None):
        self.feature = feature
        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['lease_remain_years'] = 99 - (int(datetime.today().year) - X[self.feature].astype('int64'))
        return X

class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, features_to_drop=None):
        
        self.features = features_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.drop(self.features, axis=1)

        return X