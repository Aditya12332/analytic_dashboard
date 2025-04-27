from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all campaigns with optional status filtering
@router.get("/", response_model=List[schemas.Campaign])
def read_campaigns(status: str = Query(None, regex="^(Active|Paused)$"), db: Session = Depends(get_db)):
    query = db.query(models.Campaign)
    if status:
        query = query.filter(models.Campaign.status == status)
    return query.all()
