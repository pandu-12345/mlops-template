
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import RedirectResponse

from project_name.components.modelprediction import Prediction
from PIL import Image
import io


app = FastAPI()


@app.get("/")
async def redirect_to_streamlit():
    return RedirectResponse(url="http://40.81.226.190:8501") 

predictor = Prediction()  

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        result = predictor.predict_image(image)
        return result
    except Exception as e:
        return {"error": str(e)}