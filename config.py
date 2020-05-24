# data
TRAINING_DATA_FILE = "./data/preprocessed_data.csv"
PIPELINE_NAME = 'xgboost_regression'

TARGET = 'price_per_sqft'

FEATURES = ['latitude', 'longitude', 'flat_type', 'floor_area_sqm', 
       'lease_commence_date', 'storey_range']

CATEGORICAL_FEATURES = ['flat_type', 'storey_range']

TEMPORAL_FEATURES = 'lease_commence_date'

DROP_FEATURES = ['flat_type', 'storey_range']
