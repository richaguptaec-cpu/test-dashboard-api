from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from pydantic import BaseModel
from typing import List, Literal, Optional
from datetime import datetime

from app.schemas import TestResultResponse

from .database import SessionLocal
from .models import TestResult

router = APIRouter()

## Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema (Validation)  
class TestResultCreate(BaseModel):
    test_name: str
    status: Literal["PASS", "FAIL"]
    execution_time: float
    environment: str

# For updates, all fields are optional
class TestResultUpdate(BaseModel):
    test_name: Optional[str] = None
    status: Optional[Literal["PASS", "FAIL"]] = None
    execution_time: Optional[float] = None
    environment: Optional[str] = None

# API Endpoints
# POST: Add a new test result
@router.post("/test-results", response_model=TestResultResponse)
def add_test_result(data: TestResultCreate, db: Session = Depends(get_db)):
    test = TestResult(**data.model_dump())
    db.add(test)
    db.commit()
    db.refresh(test)
    return test

# PUT: Update an existing test result (Partial Update)
@router.put("/test-results/{test_id}", response_model=TestResultResponse)
def update_test_result(
    test_id: int,
    data: TestResultUpdate,
    db: Session = Depends(get_db)
):
    test = db.query(TestResult).filter(TestResult.id == test_id).first()

    if not test:
        raise HTTPException(status_code=404, detail="Test result not found")

    # Only update fields user sends. Prevent overwriting with None.
    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(test, key, value)

    db.commit()
    db.refresh(test)

    return test

# DELETE: Delete a test result by ID
@router.delete("/test-results/{test_id}")
def delete_test_result(test_id: int, db: Session = Depends(get_db)):
    test = db.query(TestResult).filter(TestResult.id == test_id).first()

    if not test:
        raise HTTPException(status_code=404, detail="Test result not found")

    db.delete(test)
    db.commit()

    return {"message": "Test result deleted successfully"}

# GET: All Results (Filter + Sort + Limit)
@router.get("/test-results", response_model=List[TestResultResponse])
def get_results(status: Optional[str] = None, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(TestResult)

    if status:
        query = query.filter(TestResult.status == status)

    # Sort by latest created_at
    query = query.order_by(desc(TestResult.created_at))

    return query.limit(limit).all()

# GET: Result by ID
@router.get("/test-results/{test_id}", response_model=TestResultResponse)
def get_test_result(test_id: int, db: Session = Depends(get_db)):
    test = db.query(TestResult).filter(TestResult.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Test result not found")
    return test

# GET: Summary (Total, Passed, Failed, Pass Rate)
@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total = db.query(TestResult).count()
    passed = db.query(TestResult).filter(TestResult.status == "PASS").count()
    failed = db.query(TestResult).filter(TestResult.status == "FAIL").count()

    pass_rate = (passed / total * 100) if total > 0 else 0

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate":round(pass_rate, 2)
    }