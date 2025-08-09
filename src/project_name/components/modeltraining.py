from ..entity.config_entity import trainingEntity
import torch
from torch import nn, optim
from torchvision import transforms,datasets,models
import numpy as np
from torch.utils.data import DataLoader
import mlflow
import mlflow.pytorch
from dotenv import load_dotenv
import os

class ModelTraining:
    def __init__(self,trainingEntity:trainingEntity):
        self.entity = trainingEntity
        dotenv_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
        )
        load_dotenv(dotenv_path=dotenv_path) 
        self.mlflow_uri = os.getenv("MLFLOW_TRACKING_URI")
        self.experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME")
        self.registered_model_name = os.getenv("MLFLOW_REGISTERED_MODEL_NAME")

    def train(self):
        
        transform = transforms.Compose([
            transforms.Resize(self.entity.image_size),
            transforms.ToTensor()
        ])

        dataset = datasets.ImageFolder(root= self.entity.training_data,transform= transform)
        dataloader = DataLoader(dataset, batch_size=self.entity.batch_size, shuffle= True)

        model= models.resnet18(weights=None)
        model.fc= nn.Linear(model.fc.in_features,self.entity.num_classes) 

        criterion= nn.CrossEntropyLoss()
        optimizer= optim.Adam(model.parameters(), lr=self.entity.learning_rate)

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        mlflow.set_tracking_uri(self.mlflow_uri)
        mlflow.set_experiment(self.experiment_name)

        with mlflow.start_run():
            # Log static parameters once
            mlflow.log_param("Batch_size", self.entity.batch_size)
            mlflow.log_param("Learning_rate", self.entity.learning_rate)
            mlflow.log_param("Epochs", self.entity.epochs)
            mlflow.log_param("Image_size", self.entity.image_size)

            model.train()
            for epoch in range(self.entity.epochs):
                total_loss = 0.0
                correct = 0
                total = 0

                for images, labels in dataloader:
                    images, labels = images.to(device), labels.to(device)

                    optimizer.zero_grad()
                    outputs = model(images)
                    loss = criterion(outputs, labels)
                    loss.backward()
                    optimizer.step()

                    total_loss += loss.item()
                    _, predicted = torch.max(outputs, 1)
                    correct += (predicted == labels).sum().item()
                    total += labels.size(0)

                accuracy = correct / total
                print(f"Epoch {epoch+1}/{self.entity.epochs}, Loss: {total_loss:.4f}, Accuracy: {accuracy:.4f}")

                mlflow.log_metric("Loss", total_loss, step=epoch)
                mlflow.log_metric("Accuracy", accuracy, step=epoch)



            input_examples = torch.rand(1, 3, self.entity.image_size[0], self.entity.image_size[1])
            if isinstance(input_examples, torch.Tensor):
                input_examples = input_examples.detach().cpu().numpy()
            elif not isinstance(input_examples, np.ndarray):
                raise TypeError(f"input_example must be torch.Tensor or numpy.ndarray, got {type(input_examples)}")

            # Log model to MLflow
            print("DEBUG: input_example type is",type(input_examples))
            print("DEBUG: code version marker v2")
            mlflow.pytorch.log_model(
                model,
                name="model", 
                input_example=input_examples.astype(np.float32),
                registered_model_name=self.registered_model_name
            )

            

            # Save class mapping
            mlflow.log_dict(dataset.class_to_idx, "class_to_idx.json")

            torch.save(model.state_dict(), self.entity.model_dir)
            print(f"Model saved to {self.entity.model_dir}")