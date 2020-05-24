import xgboost as xgb
from sklearn.pipeline import Pipeline
from datetime import datetime

import preprocessors as pp
import config


resale_pipe = Pipeline(
    [
        ('categorical_encoder',
            pp.CategoricalEncoder(features=config.CATEGORICAL_FEATURES)
        ),
        ('temporal_encoder',
            pp.TemporalEncoder(feature=config.TEMPORAL_FEATURES)
        ),
        ('drop_features',
            pp.DropUnecessaryFeatures(features_to_drop=config.DROP_FEATURES)
        ),
        ('xgboost_reg',
            xgb.XGBRegressor(objective="reg:squarederror",n_estimator=10,seed=123)
        )
    ]
)
