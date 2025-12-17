from MLProject_mlflow.config.configuration import ConfigurationManager
from MLProject_mlflow.components.data_transformation import DataTransformation
from MLProject_mlflow import logger
from pathlib import Path


STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split()


if __name__ == "__main__":
    try:
        logger.info(">>>>>> {STAGE_NAME} Started<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(">>>>>> {STAGE_NAME} Completed<<<<<<<<<\n")
    except Exception as e:
        logger.info(e)
        raise e