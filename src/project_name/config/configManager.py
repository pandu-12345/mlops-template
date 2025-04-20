import os
from ..Utills.utills import read_yaml
from ..contants import CONFIG_FILE_PATH,  PARAMS_FILE_PATH
from ..entity.config_entity import DataIngestionEntity


class ConfigManager:
    def __init__(self,config = CONFIG_FILE_PATH,params = PARAMS_FILE_PATH):
        self.config =  read_yaml(config)
        self.params = read_yaml(params)
        os.makedirs(self.config.artifact_root,exist_ok=True)

    def getdataingestionentity(self)->DataIngestionEntity:
        config = self.config.data_ingestion
        os.makedirs(config.root_dir,exist_ok=True)
        dataingestionentity = DataIngestionEntity(
            source_url= config.source_url,
            root_dir= config.root_dir,
            Unzip_dir= config.unzip_data_file,
            zip_dir= config.zip_data_file
        )
        return dataingestionentity
    