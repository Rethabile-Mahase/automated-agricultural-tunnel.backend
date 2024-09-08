from app import db
from sqlalchemy import DOUBLE_PRECISION, func


class Sensor(db.Model):
    __tablename__ = 'Sensor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    humidity = db.Column(db.Integer, nullable=True)
    temperature = db.Column(DOUBLE_PRECISION, nullable=True)
    soilMoistureContent = db.Column(DOUBLE_PRECISION, nullable=True)
    waterFlow = db.Column(DOUBLE_PRECISION, nullable=True)

    def __init__(self, humidity, temperature, soil_moisture_content, water_flow):
        self.humidity = humidity
        self.temperature = temperature
        self.soilMoistureContent = soil_moisture_content
        self.waterFlow = water_flow

    def save(self):
        db.session.add(self)
        db.session.commit()


