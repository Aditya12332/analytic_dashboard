from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app import models
from app.routers import campaigns

# Create tables if not already present
models.Base.metadata.create_all(bind=engine)

# FastAPI app initialization
app = FastAPI(redirect_slashes=False)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
def create_seed_data():
    db = SessionLocal()

    # List of campaigns to be added
    campaigns_data = [
        models.Campaign(name="Summer Sale", status="Active", clicks=150, cost=45.99, impressions=1000),
        models.Campaign(name="Black Friday", status="Paused", clicks=320, cost=89.50, impressions=2500),
        models.Campaign(name="Holiday Promo", status="Active", clicks=200, cost=75.00, impressions=1500),
        models.Campaign(name="New Year Blast", status="Paused", clicks=50, cost=25.00, impressions=500),
        models.Campaign(name="Spring Launch", status="Active", clicks=120, cost=60.00, impressions=900),
        models.Campaign(name="Flash Deal", status="Paused", clicks=80, cost=30.00, impressions=700),
        models.Campaign(name="Back to School", status="Active", clicks=300, cost=95.00, impressions=2000),
        models.Campaign(name="Cyber Monday", status="Paused", clicks=400, cost=120.00, impressions=3000),
        models.Campaign(name="Year End", status="Active", clicks=180, cost=70.00, impressions=1300),
        models.Campaign(name="Summer Finale", status="Paused", clicks=90, cost=35.00, impressions=800)
    ]

    # Add or update campaigns (upsert) - Prevent duplicates based on the campaign name
    for campaign in campaigns_data:
        # Check if the campaign already exists by name
        existing_campaign = db.query(models.Campaign).filter(models.Campaign.name == campaign.name).first()
        
        if existing_campaign:
            # If it exists, update the fields of the existing campaign
            existing_campaign.status = campaign.status
            existing_campaign.clicks = campaign.clicks
            existing_campaign.cost = campaign.cost
            existing_campaign.impressions = campaign.impressions
        else:
            # If it does not exist, insert a new campaign
            db.add(campaign)
    
    db.commit()
    db.close()

# Add seed data when the app starts (only if data does not already exist)
create_seed_data()

# Include the campaigns router
app.include_router(campaigns.router, prefix="/campaigns", tags=["campaigns"])
