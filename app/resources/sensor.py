from flask_restx import Resource, fields, Namespace
from app.models.sensor import Sensor

sensor_ns = Namespace('sensor', description='Operations related to sensor data')

sensor_details = sensor_ns.model('sensor', {
    'humidity': fields.String(),
    'temperature': fields.String(),
    'soilMoistureContent': fields.String(),
    'waterFlow': fields.String(),
})


@sensor_ns.route('/')
class SensorResource(Resource):
    @sensor_ns.expect(sensor_details)
    @sensor_ns.doc()
    def post(self):
        if not sensor_ns.payload:
            return {'message': 'internal server error'}, 500
        humidity = sensor_ns.payload.get('humidity')
        temperature = sensor_ns.payload.get('temperature')
        soil_moisture_content = sensor_ns.payload.get('soilMoistureContent')
        water_flow = sensor_ns.payload.get('waterFlow')
        sensor = Sensor(humidity, temperature, soil_moisture_content, water_flow)
        sensor.save()
        return {'message': 'data successfully posted'}, 200

    @sensor_ns.doc()
    def get(self):
        last_sensor = Sensor.query.order_by(Sensor.id.desc()).first()
        if not last_sensor:
            return {'message': 'No data found'}, 404
        response = {
            'humidity': last_sensor.humidity,
            'temperature': last_sensor.temperature,
            'soilMoistureContent': last_sensor.soilMoistureContent,
            'waterFlow': last_sensor.waterFlow
        }
        return response, 200


