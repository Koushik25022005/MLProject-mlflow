import os 
from MLProject_mlflow import logger
from MLProject_mlflow.entity.config_enity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_cols(self) -> bool:
        try:
            validation_stat = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_stat = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_stat}")
                else:
                    validation_stat = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_stat}")
            return validation_stat
        except Exception as e:
            raise e