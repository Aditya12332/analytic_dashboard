from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app import models
from app.routers import campaigns

# Create tables if not already present
models.Base.metadata.create_all(bind=engine)

# FastAPI app initialization (disable global slash-redirect)
app = FastAPI(redirect_slashes=False)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods including OPTIONS
    allow_headers=["*"],   # Allow all headers
)

# Seed data function (runs at startup)
def create_seed_data():
    db = SessionLocal()
    try:
        campaigns_data = [
            models.Campaign(name="Summer Sale", status="Active", clicks=150, cost=45.99, impressions=1000),
            # ... other campaigns
        ]
        for campaign in campaigns_data:
            existing = db.query(models.Campaign).filter(models.Campaign.name == campaign.name).first()
            if existing:
                existing.status = campaign.status
                existing.clicks = campaign.clicks
                existing.cost = campaign.cost
                existing.impressions = campaign.impressions
            else:
                db.add(campaign)
        db.commit()
    finally:
        db.close()

# Run seed on startup
def startup_event():
    create_seed_data()

app.add_event_handler("startup", startup_event)

# Include campaigns router (prefix already set in router)
app.include_router(campaigns.router)
