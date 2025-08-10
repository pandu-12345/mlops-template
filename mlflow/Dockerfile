FROM python:3.12-slim

RUN pip install mlflow[extras] boto3

WORKDIR /mlflow

CMD ["mlflow", "server","--host", "0.0.0.0","--port", "5000","--backend-store-uri", "sqlite:///mlflow.db","--default-artifact-root", "wasbs://mlflow@mlflowartifactsud.blob.core.windows.net/"]
