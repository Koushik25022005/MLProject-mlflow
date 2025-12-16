from MLProject_mlflow import logger
from MLProject_mlflow.config.configuration import ConfigurationManager
from MLProject_mlflow.components.data_validation import DataValidation


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_cols()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} Started <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> {STAGE_NAME} Completed <<<<<<<<<<\n")
    except Exception as e:
        logger.info(e)
        raise e