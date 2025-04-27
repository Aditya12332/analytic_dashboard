from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app import models
from app.routers import campaigns

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# Function to add seed data to the database
def create_seed_data():
    db = SessionLocal()

    if not db.query(models.Campaign).first():
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
        
        db.add_all(campaigns_data)
        db.commit()
    
    db.close()

create_seed_data()


app.include_router(campaigns.router, prefix="/campaigns", tags=["campaigns"])
