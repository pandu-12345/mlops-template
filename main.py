from project_name import ConfigManager
from project_name import DataIngestion
from project_name import DataTransformation
from project_name import ModelTraining
from project_name import ModelEvaluation

configManager = ConfigManager()
dataingestion_entity = configManager.get_dataingestion_entity()
dataIngestioncomponent = DataIngestion(dataingestion_entity)
dataIngestioncomponent.download_data()
dataIngestioncomponent.extract_data()

datatransformationentity = configManager.get_data_transformation_entity()
datatransformation= DataTransformation(datatransformationentity)
datatransformation.transform()

modeltrainingentity= configManager.get_training_entity()
component = ModelTraining(modeltrainingentity)
component.train()

modelevaluationentity= configManager.get_evaluation_entity()
modelevaluation= ModelEvaluation(modelevaluationentity)
modelevaluation.evaluate()