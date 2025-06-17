#utils.py
#example utils.py file
#create a mogodb client connection
#save my model in to the cloud

import os
import sys 
import numpy as np
import pandas as pd 
import src.exception as CustomException
import dill
import pickle

    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)