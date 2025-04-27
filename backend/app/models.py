from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String(10), nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    impressions = Column(Integer, nullable=False)
