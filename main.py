
from flask import Flask
import logging
from controller.measurement_controller import MeasurementController
import os
from service.reporting_service import ReportingService
from repository.reporting_repository import ReportingRepository


# Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    try:
        reporting_repository = ReportingRepository()
        reporting_service = ReportingService(reporting_repository)
        measurement_controller = MeasurementController(reporting_service)
        app.register_blueprint(measurement_controller.blueprint, url_prefix='/api')
    except Exception as e:
        logging.error(f'Error setting up controllers: {e}')
        raise

    return app


def run_app(app):
    """Run the Flask application with configurations from environment variables."""
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5001))
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

    app.run(host=host, port=port, debug=debug_mode)


if __name__ == '__main__':
    app = create_app()
    run_app(app)

