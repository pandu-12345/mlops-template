#This is utills
from pathlib import Path
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
def read_yaml(config_file:Path)->ConfigBox:
    try:
        with open(config_file) as f:
            content = yaml.safe_load(f)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
