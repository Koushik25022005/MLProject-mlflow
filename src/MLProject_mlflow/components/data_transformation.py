from MLProject_mlflow import logger
import os
from sklearn.model_selection import train_test_split
import pandas as pd
from MLProject_mlflow.entity.config_enity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

# You can add methods for transformation such as Scaler, Imputer, PCA etc.
# You can perform all kinds of EDA in the ML cycle before passing this data to the model

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Train test split is completed.")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)