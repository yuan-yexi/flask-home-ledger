from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Create DB instance
db = SQLAlchemy(app)


class HdbPropertyInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blk = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    year_completed = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.Float(100))
    lng = db.Column(db.Float(100))

    def __reper__(self):
        return f"HdbPropertyInfo('{self.id}', '{self.blk}', '{self.street}', '{self.year_completed}', '{self.lat}', '{self.lng}' )"

class ModelPredictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    blk = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    floor_area_sqm = db.Column(db.Integer, nullable=False)
    flat_type = db.Column(db.String(100), nullable=False)
    storey_range = db.Column(db.String(100), nullable=False)
    lease_commence_date = db.Column(db.Float(100), nullable=False)
    lat = db.Column(db.Float(100), nullable=False)
    lng = db.Column(db.Float(100), nullable=False)
    prediction = db.Column(db.Float(100), nullable=False)

    def __reper__(self):
        return f"Prediction('{self.prediction}')"
