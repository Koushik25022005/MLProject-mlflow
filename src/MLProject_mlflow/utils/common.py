import os
from box.exceptions import BoxValueError
import yaml
from MLProject_mlflow import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args: path_to_yaml (str)

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
    ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file: 
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    creates a list of directories

    Args:
        path_to_directories (list):list of path of directories
        ignore_log (bool): ignore if multiple dirs is to be created. Defaults to False

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at path: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """ Saves json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

       
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    loads json files data

    Args:
        path ( Path): path to json file

    Returns:
        ConfigbOX: data as class attributes instead of dict
    """
    with open(path) as p:
        content = json.load(p)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ save binary file
    Args:
        data (Any): data to be saved
        path (Path): path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ loads binary data from a file
    Args:
        path (Path): path to the binary
    Returns:
        Any: data loaded from the binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """ get size of a file in kb
    Args:
        path (Path): path to the file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"