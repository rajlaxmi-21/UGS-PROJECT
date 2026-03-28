from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deforestation Monitoring API is running 🚀"}

@app.post("/analyze-location")
def analyze_location():
    return {"status": "analysis started"}

@app.post("/add-permit")
def add_permit():
    return {"status": "permit added"}

@app.get("/trend-data")
def trend_data():
    return {"data": "trend data"}