import mlflow
import mlflow.pytorch
from ..Utills.utills import read_yaml
from ..contants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from PIL import Image
import torch
from torchvision import transforms
import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
)

load_dotenv(dotenv_path=dotenv_path) 

class Prediction:
    def __init__ (self,config = CONFIG_FILE_PATH,params = PARAMS_FILE_PATH):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.params = read_yaml(params)
        self.config = read_yaml(config)
        
        tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
        model_name = os.getenv("MLFLOW_MODEL_NAME")
        model_stage = os.getenv("MLFLOW_MODEL_STAGE","production")


        if not all([tracking_uri, model_name, model_stage]):
            raise EnvironmentError("Missing one of the required environment variables: MLFLOW_TRACKING_URI, MLFLOW_MODEL_NAME, MLFLOW_MODEL_STAGE")
        
        # Set MLflow tracking URI and load model
        mlflow.set_tracking_uri(tracking_uri)
        self.model = mlflow.pytorch.load_model(model_uri=f"models:/{model_name}@{model_stage}")
        self.model.to(self.device)
        self.model.eval()


        self.transform = transforms.Compose([
            transforms.Resize(tuple(self.params["image_size"])),
            transforms.ToTensor()
        ])

    def predict_image(self, image: Image.Image):
        try:
            img_tensor = self.transform(image).unsqueeze(0).to(self.device)
            with torch.no_grad():
                output = self.model(img_tensor)
                prediction = torch.argmax(output, dim=1).item()
            return {"prediction": prediction}
        except Exception as e:
            return {"error": str(e)}


