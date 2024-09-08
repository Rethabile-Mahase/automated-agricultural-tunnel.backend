from flask_restx import Resource, fields, Namespace
from app.models.actuator import Actuator

actuator_ns = Namespace('actuator', description='Operations related to actuator data')

actuator_details = actuator_ns.model('actuator', {
    'fanStatus': fields.String(),
    'flapperStatus': fields.String(),
    'sprinklerStatus': fields.String(),
    'heaterStatus': fields.String()
})


@actuator_ns.route('/')
class ActuatorResource(Resource):
    @actuator_ns.expect(actuator_details)
    @actuator_ns.doc()
    def post(self):
        if not actuator_ns.payload:
            return {'message': 'internal server error'}, 500
        fan_status = flapper_status = sprinkler_status = heater_status = False
        if actuator_ns.payload.get('fanStatus') == '1':
            fan_status = True
        if actuator_ns.payload.get('flapperStatus') == '1':
            flapper_status = True
        if actuator_ns.payload.get('sprinklerStatus') == '1':
            sprinkler_status = True
        if actuator_ns.payload.get('heaterStatus') == '1':
            heater_status = True
        actuator = Actuator(fan_status, flapper_status, sprinkler_status, heater_status)
        actuator.save()
        return {'message': 'data successfully posted'}, 200

    @actuator_ns.doc()
    def get(self):
        last_actuator = Actuator.query.order_by(Actuator.id.desc()).first()
        if not last_actuator:
            return {'message': 'No data found'}, 404
        return {
            'fanStatus': last_actuator.fanStatus,
            'flapperStatus': last_actuator.flapperStatus,
            'sprinklerStatus': last_actuator.sprinklerStatus,
            'heaterStatus': last_actuator.heaterStatus
        }