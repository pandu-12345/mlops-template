import os
from pathlib import Path
from PIL import Image

from ..entity.config_entity import dataTransformEntity
class DataTransformation:
    def __init__(self,entity:dataTransformEntity):
        self.datatransformentity= entity
        
    def transform(self):
        if self.datatransformentity.data_type == 'image':
            self._transform_images()
        elif self.datatransformentity.data_type == "tebular":
            self._transform_tebular()
        else:
            print(f"data type {self.datatransformentity.data_type} not found")

    def _transform_images(self):
        input_data_file = Path(self.datatransformentity.raw_data_dirc)
        image_size = self.datatransformentity.image_size
        output_dir = Path(self.datatransformentity.transformed_data_dirc)
        
        label_map= []
        if os.path.exists(input_data_file):
            for file in input_data_file.iterdir():
                data_dir = output_dir/file.name
                data_dir.mkdir(parents=True,exist_ok=True)
                for image_file in file.iterdir():
                    try:
                        images= Image.open(image_file).convert("RGB")
                        images= images.resize(image_size)
                        save_path = data_dir/image_file.name
                        images.save(save_path)
                        label_map.append(
                            {"path": str(save_path), "label": file.name}
                        )
                        print({"path": str(save_path), "label": file.name})
                    except Exception as e:
                        print(f"fail to process imgae {image_file.name} : {e}")
        else:
            print(f"path {input_data_file} deos not exists")
