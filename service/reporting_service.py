import logging
from repository.reporting_repository import ReportingRepository

logger = logging.getLogger(__name__)


class ReportingService:

    def __init__(self, reporting_repository: ReportingRepository):
        logger.info("ReportingService initialized")
        self.reporting_repository = reporting_repository

    def get_device_measurements(self, device_identifier, num_measurements):
        try:
            if not device_identifier or not isinstance(num_measurements, int):
                raise ValueError("Invalid input parameters")
            return self.reporting_repository.get_measurements(device_identifier, num_measurements)
        except Exception as e:
            logger.error(f"Error in get_device_measurements: {e}")
            raise
