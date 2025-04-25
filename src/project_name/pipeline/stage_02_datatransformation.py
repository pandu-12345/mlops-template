

from ..components.datatransformation import DataTransformation
from ..config.configManager import ConfigManager


class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        configManager= ConfigManager()
        datatransformationentity = configManager.get_data_transformation_entity()
        datatransformation= DataTransformation(datatransformationentity)
        datatransformation.transform()


if __name__ == '__main__':
    print("starting data tranformation step")
    try:
        obj= DataTransformationPipeline()
        obj.main()
        print("Data transformation completed")
    except Exception as e:
        raise e