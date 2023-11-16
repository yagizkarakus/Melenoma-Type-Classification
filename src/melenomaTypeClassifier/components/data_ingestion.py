import os 
import gdown
import zipfile
from cancerDetection import logger
from cancerDetection.utils.common import get_size
from melenomaTypeClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            url = self.config.source_URL
            output = self.config.local_data_file
            _, filename = os.path.split(output)
            gdown.download(url, output, quiet=False)
            
            logger.info(f"{filename} downloaded!")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)            