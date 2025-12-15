from MLProject_mlflow.constants import *
from MLProject_mlflow.utils.common import read_yaml, create_directories
from MLProject_mlflow.entity.config_enity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
             root_dir=Path(config.root_dir),
             source_URL=config.source_URL,
             local_data_file=Path(config.local_data_file),
             unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config