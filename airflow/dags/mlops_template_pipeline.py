from airflow import DAG
from airflow.operators.python_operator import PythonOperator  
from project_name.pipeline.stage_01_dataingestion import DataIngestionPipeline
from project_name.pipeline.stage_02_datatransformation import DataTransformationPipeline
from project_name.pipeline.stage_03_model_training import ModelTrainingPipeline
from project_name.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from datetime import datetime, timedelta  


def dataingestion():
    obj = DataIngestionPipeline()
    return obj.main()

def datatransform():
    obj = DataTransformationPipeline()
    return obj.main()

def modeltraining():
    obj = ModelTrainingPipeline()
    return obj.main()

def modelevaluation():
    obj = ModelEvaluationPipeline()
    return obj.main()


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ml_pipeline',  
    default_args=default_args,
    description='End-to-end ML pipeline',
    schedule_interval=None,
    catchup=False
) as dag:
    
    data_download = PythonOperator(
        task_id="data_ingestion",
        python_callable=dataingestion
    )

    data_processing = PythonOperator(  
        task_id="data_processing",
        python_callable=datatransform
    )

    model_training = PythonOperator(  
        task_id="model_training",
        python_callable=modeltraining
    )

    model_evaluation = PythonOperator(  
        task_id="model_evaluation",
        python_callable=modelevaluation 
    )

    data_download >> data_processing >> model_training >> model_evaluation