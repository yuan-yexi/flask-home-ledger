from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
import json
import requests
import os

app = Flask(__name__)

_resale_price = joblib.load(filename='xgboost_regression')

# Get all products
@app.route('/predict', methods=['POST'])
def predict_price():
    flat_type = request.json['flat_type']
    storey_range = request.json['storey_range']
    floor_area_sqm = request.json['floor_area_sqm']
    street_name = request.json['street_name']
    block = request.json['block']
    
    address = block + ' ' + street_name

    query_string_lat_lng = 'https://developers.onemap.sg/commonapi/search?searchVal='+str(address)+'&returnGeom=Y&getAddrDetails=Y'
    resp_lease = requests.get(query_string_lat_lng)
    lat_lng_data = json.loads(resp_lease.content)
    latitude = float(lat_lng_data['results'][0]['LATITUDE'])
    longitude = float(lat_lng_data['results'][0]['LONGITUDE'])

    query_string_lease_commence = 'https://data.gov.sg/api/action/datastore_search?resource_id=482bfa14-2977-4035-9c61-c85f871daf4e&q='+str(address)
    resp_lease = requests.get(query_string_lease_commence)
    lease_data = json.loads(resp_lease.content)
    lease_commence_date = int(lease_data['result']['records'][0]['year_completed'])

    input_data = pd.DataFrame({
        "latitude": latitude,
        "longitude": longitude,
        "flat_type": flat_type,
        "floor_area_sqm":  floor_area_sqm,
        "lease_commence_date": lease_commence_date,
        "storey_range": storey_range
    }, index=[0])

    results = _resale_price.predict(input_data)
    pred = results.tolist()
    return jsonify(pred)

if __name__ == '__main__':
    app.run(port=5050,debug=True)