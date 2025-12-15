from MLProject_mlflow import logger
from MLProject_mlflow.config.configuration import ConfigurationManager
from MLProject_mlflow.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} STARTED <<<<<<<<")
        OBJ = DataIngestionTrainingPipeline()
        OBJ.main()
        logger.info(f">>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<\n")
    except Exception as e:
        logger.info(e)
        raise e