import os
from pathlib import Path
from ..Utills.utills import read_yaml
from ..contants import CONFIG_FILE_PATH,  PARAMS_FILE_PATH
from ..entity.config_entity import DataIngestionEntity, dataTransformEntity, modelevaluationentity, trainingEntity


class ConfigManager:
    def __init__(self,config = CONFIG_FILE_PATH,params = PARAMS_FILE_PATH):
        self.config =  read_yaml(config)
        self.params = read_yaml(params)
        os.makedirs(self.config.artifact_root,exist_ok=True)

    def get_data_ingestion_entity(self)->DataIngestionEntity:
        config = self.config.data_ingestion
        os.makedirs(config.root_dir,exist_ok=True)
        dataingestionentity = DataIngestionEntity(
            source_url= config.source_url,
            root_dir= Path(config.root_dir),
            Unzip_dir= Path(config.unzip_data_file),
            zip_dir= Path(config.zip_data_file)
        )
        return dataingestionentity
    
    def get_data_transformation_entity(self)->dataTransformEntity:
        config = self.config.data_transformation
        os.makedirs(config.root_dir,exist_ok=True)
        entity = dataTransformEntity(
            data_type = config.data_type,
            raw_data_dirc= os.path.join(config.unzip_data_file,"Chicken-fecal-images"),
            transformed_data_dirc = Path(config.transformed_data_file),
            image_size= config.image_size,
        )
        return entity
    
    def get_training_entity(self)->trainingEntity:

        config =self.config.model_training
        params = self.params

        entity = trainingEntity(
            model_dir= Path(config.model_dir),
            training_data= Path(config.data_dir),
            epochs= params.epochs,
            batch_size= params.batch_size,
            learning_rate= params.learning_rate,
            image_size= params.image_size,
            num_classes = params.num_classes
        )
        return entity

    def get_evaluation_entity(self):
        config= self.config.model_evaluation
        entity = modelevaluationentity(
            model_path= config.model_dir,
            test_data_path= config.data_dir,
            image_size= self.params.image_size,
            batch_size= self.params.batch_size
        )
        return entity