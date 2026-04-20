from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone
from .database import Base

class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String)
    status = Column(String)
    execution_time = Column(Float)
    environment = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))