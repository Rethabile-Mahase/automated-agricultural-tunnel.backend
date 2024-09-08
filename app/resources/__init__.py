from flask import Blueprint
from flask_restx import Api
from .sensor import sensor_ns
from .actuator import actuator_ns

api_bp = Blueprint('resources', __name__, url_prefix='/api/v1')

api = Api(api_bp,
          version='1.0.0',
          title='Agricultural tunnel',
          )

api.add_namespace(sensor_ns)
api.add_namespace(actuator_ns)
