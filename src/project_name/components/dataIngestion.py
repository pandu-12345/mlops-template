import os
from pathlib import Path
import zipfile

import requests

from ..entity.config_entity import DataIngestionEntity


class DataIngestion:
    def __init__(self,dataingestionentity:DataIngestionEntity):
        self.dataingestionentity = dataingestionentity
    def download_data(self):
        filename = Path(self.dataingestionentity.zip_dir)
        if not filename.exists():
            try:
                response = requests.get(self.dataingestionentity.source_url)
                with open(filename, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                print("cant get the data from link")
                raise e

    def extract_data(self):
        unzip_dir = self.dataingestionentity.Unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)
        zip_file_path = Path(self.dataingestionentity.zip_dir)
        if Path(zip_file_path).exists():
            # Extract the ZIP file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
                print(f"ZIP file extracted to: {unzip_dir}")
        else:
            print(f"ZIP file not found at: {zip_file_path}")