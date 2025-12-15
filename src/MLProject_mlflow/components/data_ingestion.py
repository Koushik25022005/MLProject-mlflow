import os
import requests
import zipfile
from MLProject_mlflow import logger
from MLProject_mlflow.utils.common import get_size
from MLProject_mlflow.entity.config_enity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL)
            response.raise_for_status()
            with open(self.config.local_data_file, 'wb') as f:
                f.write(response.content)
            logger.info(f"Downloaded {self.config.local_data_file}")
        else:
            logger.info(f"file already exists of size: {get_size(self.config.local_data_file)}")


    def extract_zip_file(self):
        """ Extracts the contents of the zip file into the data directory
        Function returns None"""
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)