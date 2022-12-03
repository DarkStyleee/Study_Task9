from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from db import Base


metadata = Base.metadata


class TableCounter(Base):
    __tablename__ = "tablecounter"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    client_info = Column(String)