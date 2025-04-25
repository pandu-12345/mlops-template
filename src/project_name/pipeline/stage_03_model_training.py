


from ..components.modeltraining import ModelTraining
from ..config.configManager import ConfigManager


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        modeltrainingentity= ConfigManager.get_training_entity()
        component = ModelTraining(modeltrainingentity)
        component.train()



if __name__=='__main__':
    print("Starting Model Training")
    try:
        obj= ModelTrainingPipeline()
        obj.main()
        print("model training completed")
    except Exception as e:
        raise e