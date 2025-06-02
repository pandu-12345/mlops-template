import os
from pathlib import Path
main = "project_name"
files_path = [
    f"src/{main}/__init__.py",
    f"src/{main}/Utills/utills.py",
    f"src/{main}/Utills/__init__.py",
    "Readme.md",
    "setup.py",
    "config/config.yaml",
    "params/params.yaml",
    f"src/{main}/components/__init__.py",
    "requirements.txt",
    "requirements-dev.txt",
    "experiments/trails.ipynb",
    "templates/index.html",
    f"src/{main}/entity/__init__.py",
    f"src/{main}/entity/config_entity.py",
    f"src/{main}/contants/__init__.py",
    f"src/{main}/config/__init__.py",
    f"src/{main}/config/configManager.py",
    "main.py"



]

for filepath in files_path:

    filepath = Path(filepath)
    filedirec, filename = os.path.split(filepath)

    if filedirec != "" :
        os.makedirs(filedirec, exist_ok= True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0) :
        with open(filepath , "w") as f:
            pass

    else :
        print("File already exists")