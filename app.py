
from fastapi import FastAPI,UploadFile,File
import torchvision.transforms as transforms
import mlflow.pytorch
from PIL import Image
import io
import torch
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")

app = FastAPI()

model= mlflow.pytorch.load_model("models:/MLOPs Template/Production")
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

@app.get("/")
def home():
    return "its home page" 

@app.post("/predict")
async def predictImage(file: UploadFile = File(...)):

    content= await file.read()
    image= Image.open(io.BytesIO(content)).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image_tensor)
        predicted = torch.argmax(output, dim=1).item()

    return {"predicted":predicted}