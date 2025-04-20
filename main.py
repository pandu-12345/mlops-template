from project_name import ConfigManager
from project_name import DataIngestion

configManager = ConfigManager()
dataingestion_entity = configManager.getdataingestionentity()
dataIngestioncomponent = DataIngestion(dataingestion_entity)
dataIngestioncomponent.download_data()
dataIngestioncomponent.extract_data()