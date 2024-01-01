
from datetime import datetime
from pydantic import BaseModel


class IOTMeasurementResponseDTO(BaseModel):
    value: float
    created_date: datetime = None

