from ..entity.config_entity import trainingEntity
import torch
from torch import nn, optim
from torchvision import transforms,datasets,models
from torch.utils.data import DataLoader
import mlflow
import mlflow.pytorch

class ModelTraining:
    def __init__(self,trainingEntity:trainingEntity):
        self.entity = trainingEntity

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

        model.train()

        mlflow.set_experiment("MLOPs Template")
        for epoch in range(self.entity.epochs):
            
            mlflow.log_param("Batch_size",self.entity.batch_size)
            mlflow.log_param("Learning rate", self.entity.learning_rate)
            mlflow.log_param("Epochs", self.entity.epochs)
            mlflow.log_param("Image size", self.entity.image_size)

            total_loss= 0.0
            correct= 0
            total= 0

            for images,labels in dataloader:
                images, labels = images.to(device), labels.to(device)
                optimizer.zero_grad()
                outputs = model(images)
                #print(outputs,labels)
                loss= criterion(outputs,labels)
                loss.backward()
                optimizer.step()
                total_loss+=loss.item()
                _,predicted = torch.max(outputs, 1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)

            acc = correct / total
            print(f"Epoch {epoch+1}: Loss={total_loss:.4f}, Accuracy={acc:.4f}")

            mlflow.log_metric("loss", total_loss, step=epoch)
            mlflow.log_metric("accuracy", acc, step=epoch)

            print(f"Epoch {epoch+1}/{self.entity.epochs}, Loss: {total_loss:.4f}")
        input_example = torch.rand(1, 3, 224, 224).to(device).cpu().numpy()
        mlflow.pytorch.log_model(model, artifact_path="model",input_example= input_example)
        
        class_to_idx = dataset.class_to_idx
        mlflow.log_dict(class_to_idx, "class_to_idx.json")

        torch.save(model.state_dict(),self.entity.model_dir)
        print(f"Model saved to {self.entity.model_dir}")