# Database Classes
class processed_hdb_resale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _id = db.Column(db.Integer)
    address = db.Column(db.String(150))
    block = db.Column(db.String(25))
    street_name = db.Column(db.String(150))
    postal_code = db.Column(db.String(10))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    town = db.Column(db.String(50))
    flat_type = db.Column(db.String(50))
    flat_model = db.Column(db.String(150))
    storey_range = db.Column(db.String(150))
    floor_area_sqm = db.Column(db.Integer)
    resale_price = db.Column(db.Float)
    month = db.Column(db.String(25))
    remaining_lease = db.Column(db.String(50))
    lease_commence_date = db.Column(db.String(50))
    nearest_mrt_dist = db.Column(db.Float)
    nearest_mall_dist = db.Column(db.Float)
    nearest_ga_pri_sch_dist = db.Column(db.Float)
    nearest_gf_pri_sch_dist = db.Column(db.Float)
    nearest_sap_pri_sch_dist = db.Column(db.Float)

    def __init__(self, _id, address, block, street_name, postal_code, latitude, longitude,
    town, flat_type, flat_model, storey_range, floor_area_sqm, resale_price, month, remaining_lease,
    lease_commence_date, nearest_mrt_dist, nearest_mall_dist, nearest_ga_pri_sch_dist,
    nearest_gf_pri_sch_dist, nearest_sap_pri_sch_dist):
        self._id = _id
        self.address = address
        self.block = block
        self.street_name = street_name
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
        self.town = town
        self.flat_type = flat_type
        self.flat_model = flat_model
        self.storey_range = storey_range
        self.floor_area_sqm = floor_area_sqm
        self.resale_price = resale_price
        self.month = month
        self.remaining_lease = remaining_lease
        self.lease_commence_date = lease_commence_date
        self.nearest_mrt_dist = nearest_mall_dist
        self.nearest_mall_dist = nearest_mall_dist
        self.nearest_ga_pri_sch_dist = nearest_ga_pri_sch_dist
        self.nearest_gf_pri_sch_dist = nearest_gf_pri_sch_dist
        self.nearest_sap_pri_sch_dist = nearest_sap_pri_sch_dist
