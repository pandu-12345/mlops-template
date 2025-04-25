from sklearn.metrics import accuracy_score, classification_report
import mlflow
from ..entity.config_entity import modelevaluationentity
import torch
from pathlib import Path
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import mlflow.pytorch
import json

class ModelEvaluation:
    def __init__(self, entity:modelevaluationentity):
        self.entity = entity
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def evaluate(self):
   
        model = mlflow.pytorch.load_model("models:/MLOPs Template/1")  # Version 1
        model.to(self.device)
        model.eval()

        
        transform = transforms.Compose([
            transforms.Resize(self.entity.image_size),
            transforms.ToTensor()
        ])
        test_dataset = datasets.ImageFolder(self.entity.test_data_path, transform=transform)
        test_loader = DataLoader(test_dataset, batch_size=self.entity.batch_size)

        y_true, y_pred = [], []

        with torch.no_grad():
            for inputs, labels in test_loader:
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                outputs = model(inputs)
                preds = torch.argmax(outputs, dim=1)

                y_true.extend(labels.cpu().numpy())
                y_pred.extend(preds.cpu().numpy())

        acc = accuracy_score(y_true, y_pred)
        report = classification_report(y_true, y_pred, target_names=test_dataset.classes, output_dict=True)

        mlflow.log_metric("accuracy", acc)
        mlflow.log_dict(report, "classification_report.json")
        metrics = {
            'accuracy': acc,
            'report' : report
        }
        file = "evaluation_score.json"
        path= Path(self.entity.result)
        
        path.mkdir(parents=True,exist_ok=True)
        full_path= path/file
        with open(full_path,'w') as f:
            json.dump(metrics, f, indent=4)