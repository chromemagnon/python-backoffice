
from datetime import datetime
from pydantic import BaseModel


class IOTDeviceMeasurementResponseDTO(BaseModel):
    value: float
    created_date: datetime = None

