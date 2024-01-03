from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the model
loaded_modelFPS = joblib.load('model_FPS_test.pkl')  

# Define request body model
class PredictionRequest(BaseModel):
    CpuName: float
    CpuNumberOfCores: float
    CpuNumberOfThreads: float
    CpuBaseClock: float
    CpuCacheL1: float
    CpuCacheL2: float
    CpuCacheL3: float
    CpuDieSize: float
    CpuFrequency: float
    CpuMultiplier: float
    CpuMultiplierUnlocked: float
    CpuProcessSize: float
    CpuTDP: float
    CpuNumberOfTransistors: float
    CpuTurboClock: float
    GpuName: float
    GpuArchitecture: float
    GpuBandwidth: float
    GpuBaseClock: float
    GpuBoostClock: float
    GpuBusInterface: float
    GpuNumberOfComputeUnits: float
    GpuDieSize: float
    GpuDirectX: float
    GpuNumberOfExecutionUnits: float
    GpuFP32Performance: float
    GpuMemoryBus: float
    GpuMemorySize: float
    GpuMemoryType: float
    GpuOpenCL: float
    GpuOpenGL: float
    GpuPixelRate: float
    GpuProcessSize: float
    GpuNumberOfROPs: float
    GpuShaderModel: float
    GpuNumberOfShadingUnits: float
    GpuNumberOfTMUs: float
    GpuTextureRate: float
    GpuNumberOfTransistors: float
    GpuVulkan: float
    GameName: float
    GameResolution: float
    GameSetting: float

# Endpoint for predictions
@app.post("/predict")
async def predict_fps(data: PredictionRequest):
    # Convert request data to pandas DataFrame
    new_data = pd.DataFrame([data.dict()])

    # Make predictions using the loaded model
    predictions = loaded_modelFPS.predict(new_data)
    
    return {"predictions": predictions.tolist()}

# Endpoint for predictions
@app.post("/")
async def readroot(data: PredictionRequest):
    return data

