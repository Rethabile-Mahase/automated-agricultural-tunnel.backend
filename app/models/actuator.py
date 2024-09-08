from app import db
from sqlalchemy import func


class Actuator(db.Model):
    __tablename__ = 'Actuator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    fanStatus = db.Column(db.Boolean, nullable=True)
    flapperStatus = db.Column(db.Boolean, nullable=True)
    sprinklerStatus = db.Column(db.Boolean, nullable=True)
    heaterStatus = db.Column(db.Boolean, nullable=True)

    def __init__(self, fan_status, flapper_status, sprinkler_status, heater_status):
        self.fanStatus = fan_status
        self.flapperStatus = flapper_status
        self.sprinklerStatus = sprinkler_status
        self.heaterStatus = heater_status

    def save(self):
        db.session.add(self)
        db.session.commit()


