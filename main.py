from src.MLProject_mlflow import logger
from src.MLProject_mlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} STARTED <<<<<<<<")
        OBJ = DataIngestionTrainingPipeline()
        OBJ.main()
        logger.info(f">>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<\n")
    except Exception as e:
        logger.info(e)
        raise e