from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IotDevice(Base):
    __tablename__ = 'iot_device'
    id = Column(Integer, primary_key=True)
    device_identifier = Column(String(45))


class IotMeasurement(Base):
    __tablename__ = 'iot_measurement'
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer)
    value = Column(Float)
    created_date = Column(DateTime)

