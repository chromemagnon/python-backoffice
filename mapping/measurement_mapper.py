
from model.dto.measurement_response_dto import IOTMeasurementResponseDTO


class MeasurementMapper:

    @staticmethod
    def map_to_measurement_dto(rows):
        return [IOTMeasurementResponseDTO(
            value=row.value,
            created_date=row.created_date).model_dump_json()
                for row in rows]
