from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Pydantic schema (Validation)
class TestResultResponse(BaseModel):
    id: int
    test_name: str
    status: str
    execution_time: float
    environment: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)