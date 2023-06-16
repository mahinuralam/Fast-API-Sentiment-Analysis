from typing import Dict

from sqlalchemy import Column, Integer, String

from database import Base


class Analyze(Base):
    __tablename__ = "Analysis Data Table"
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    sentiment = Column(String(100))
    