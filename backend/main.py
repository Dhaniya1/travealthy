from fastapi import FastAPI, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from models.search import RouteSearch

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/search")
def save_search(
    source: str,
    destination: str,
    db: Session = Depends(get_db)
):
    search = RouteSearch(
        source=source,
        destination = destination,
        avg_aqi = 90
    )
    db.add(search)
    db.commit()
    db.refresh(search)
    return search