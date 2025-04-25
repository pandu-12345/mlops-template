from ..components.dataIngestion import DataIngestion
from ..config.configManager import ConfigManager


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigManager()
        dataingestion_entity = configManager.get_data_ingestion_entity()
        dataIngestioncomponent = DataIngestion(dataingestion_entity)
        dataIngestioncomponent.download_data()
        dataIngestioncomponent.extract_data()

if __name__=='__main__':
    print("starting data ingestion")
    try:
        obj = DataIngestionPipeline()
        obj.main()
        print("Data ingestion completed")
    
    except Exception as e:
        raise e