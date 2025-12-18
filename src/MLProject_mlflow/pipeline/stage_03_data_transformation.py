from MLProject_mlflow.config.configuration import ConfigurationManager
from MLProject_mlflow.components.data_transformation import DataTransformation
from MLProject_mlflow import logger
from pathlib import Path


STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                content = f.read()
                status = content.split(" ")[-1].strip()
                print(f"Data validation status: {status}")

                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("Your data schema is not valid.")
        except Exception as e:
            print(e)

