from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .sqlalchemy_config import Base

class School(Base):
    __tablename__ = 'SchoolsInfomation'

    id = Column(Integer, primary_key=True, index=True)
    emis_number = Column(Integer, unique=True, index=True)
    official_school_name = Column(String, index=True)
    census_area = Column(String)
    education_region = Column(String)
    circuit_cluster = Column(String)
    provincial_department = Column(String)
    education_district = Column(String)
    district_code = Column(Integer)
    postal_address_type = Column(String)
    street_name = Column(String)
    suburb = Column(String)
    town_city = Column(String)
    postal_code = Column(String)
    building_name = Column(String)
    building_number = Column(Integer)
