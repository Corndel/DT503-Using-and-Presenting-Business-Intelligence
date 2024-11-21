from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from xgboost import XGBClassifier
import uvicorn
import pandas as pd

app = FastAPI(title="Accident Risk Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RiskInput(BaseModel):
    light_conditions: int = Field(..., description="Lighting condition code (1-5)")
    weather_conditions: int = Field(..., description="Weather condition code (1-7)")
    road_surface_conditions: int = Field(
        ..., description="Road surface condition code (1-7)"
    )
    road_type: int = Field(1, description="Road type code")
    speed_limit: int = Field(30, description="Speed limit in mph")
    urban_or_rural_area: int = Field(1, description="Urban (1) or Rural (2) area")
    junction_detail: int = Field(0, description="Junction detail code")
    number_of_vehicles: int = Field(1, description="Number of vehicles involved")
    number_of_casualties: int = Field(1, description="Number of casualties")


@app.post("/predict_risk")
async def predict_risk(input_data: RiskInput):
    try:
        model = XGBClassifier()
        model.load_model("Week 4/accident_model.json")
        features = pd.DataFrame([input_data.dict()])
        risk_probs = model.predict_proba(features)[0]

        return {
            "risk_score": float(risk_probs[1]),
            "severity_probabilities": {
                "low": float(risk_probs[0]),
                "medium": float(risk_probs[1]),
                "high": float(risk_probs[2]),
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
