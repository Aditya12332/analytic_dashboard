from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app import models, schemas

# Create router with prefix, tags, and disable trailing slash redirect
template_router = APIRouter(
    prefix="/campaigns",
    tags=["campaigns"],
    redirect_slashes=False
)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Handle CORS preflight OPTIONS request explicitly
@template_router.options("/", include_in_schema=False)
async def campaigns_preflight():
    return Response(status_code=status.HTTP_200_OK)

# Get all campaigns with optional status filtering
@template_router.get("/", response_model=List[schemas.Campaign])
def read_campaigns(
    status: str = Query(None, regex="^(Active|Paused)$"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Campaign)
    if status:
        query = query.filter(models.Campaign.status == status)
    return query.all()

# Export router instance
router = template_router
