import logging
from http import HTTPStatus
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from service.reporting_service import ReportingService

logger = logging.getLogger(__name__)


class MeasurementController:
    def __init__(self, reporting_service: ReportingService):
        self.reporting_service = reporting_service
        self.blueprint = Blueprint("measurement_blueprint", __name__)
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route('/measurements/devices/<device_identifier>', methods=['GET'])
        def get_measurements_for_device(device_identifier):
            try:
                num_measurements = request.args.get('number', default=10, type=int)
                measurements = self.reporting_service.get_device_measurements(device_identifier, num_measurements)
                return jsonify(measurements), HTTPStatus.OK
            except ValidationError as e:
                logger.error(f"Validation error: {e}")
                return jsonify({"error": "Invalid request"}), HTTPStatus.BAD_REQUEST
            except ValueError as e:
                logger.error(f"Value error: {e}")
                return jsonify({"error": "Invalid request"}), HTTPStatus.INTERNAL_SERVER_ERROR
            except Exception as e:
                logger.error(f"Error getting measurements: {e}")
                return jsonify({"error": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

