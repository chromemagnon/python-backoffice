from model.dto.measurement_response_dto import IOTDeviceMeasurementResponseDTO
import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model.database.models import Base, IotDevice, IotMeasurement

logger = logging.getLogger(__name__)


class ReportingRepository:
    def __init__(self, db_url=None):
        db_url = db_url or os.getenv('DATABASE_URL')
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_measurements(self, device_identifier, num_measurements):
        session = self.Session()
        try:
            device = self.get_device(session, device_identifier)
            if not device:
                logger.warning(f"Device ID not found for identifier: {device_identifier}")
                return []

            query = session.query(IotMeasurement.value, IotMeasurement.created_date).filter(
                IotMeasurement.device_id == int(device.id)
            ).order_by(
                IotMeasurement.created_date.desc()
            ).limit(num_measurements)

            return [IOTDeviceMeasurementResponseDTO(
                value=row.value,
                created_date=row.created_date).model_dump_json()
                    for row in query.all()]
        except SQLAlchemyError as e:
            logger.error(f"Database Error in get_measurements: {e}")
            raise
        finally:
            session.close()

    def get_device(self, session, device_identifier):
        return session.query(IotDevice).filter(
            IotDevice.device_identifier == device_identifier
        ).first()

