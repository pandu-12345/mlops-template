

from ..components.modelevaluation import ModelEvaluation
from ..config.configManager import ConfigManager


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        modelevaluationentity= ConfigManager.get_evaluation_entity()
        modelevaluation= ModelEvaluation(modelevaluationentity)
        modelevaluation.evaluate()


if __name__=='__main__':
    print("starting model evaluation")
    try:
        obj= ModelEvaluationPipeline()
        obj.main()
        print("model evaluation complete")
    except Exception as e:
        raise e