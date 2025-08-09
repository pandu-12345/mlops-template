import mlflow
import mlflow.pytorch
from dotenv import load_dotenv
import os
dotenv_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
        )
load_dotenv(dotenv_path=dotenv_path) 
mlflow_uri = os.getenv("MLFLOW_TRACKING_URI")
experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME")

print(experiment_name)