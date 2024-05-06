from fastapi import FastAPI, File, Query, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse, PlainTextResponse
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(
    title="Credit Card Fraud Detection API",
    version="1.0.0", debug=True)


model = joblib.load('credit_fraud.pkl')

@app.get("/", response_class=PlainTextResponse)
async def running():
  note = """
Credit Card Fraud Detection API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
  return note

favicon_path = 'favicon.png'
@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
																	
class fraudDetection(BaseModel):
    time:float
    V1:float
    V2:float
    V3:float
    V4:float
    V5:float
    V6:float
    V7:float
    V8:float
    V9:float
    V10:float
    V11:float
    V12:float
    V13:float
    V14:float
    V15:float
    V16:float
    V17:float
    V18:float
    V19:float
    V20:float
    V21:float
    V22:float
    V23:float
    V24:float
    V25:float
    V26:float
    V27:float
    V28:float
    Amount:float

@app.post('/predict')
def predict(data: fraudDetection):
    # Prepare features for prediction
    features = np.array([[data.time, data.V1, data.V2, data.V3, data.V4, data.V5, data.V6, data.V7,
                          data.V8, data.V9, data.V10, data.V11, data.V12, data.V13, data.V14, data.V15, 
                          data.V16, data.V17, data.V18, data.V19, data.V20, data.V21, data.V22, data.V23, 
                          data.V24, data.V25, data.V26, data.V27, data.V28, data.Amount]])

    # Perform prediction using the loaded model
    predictions = model.predict(features)

    # Return prediction result
    if predictions == 1:
        return {"Fraudulent transaction"}
    else:
        return {"Legitimate transaction"}
