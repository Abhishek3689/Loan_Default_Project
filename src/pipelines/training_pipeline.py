import os,sys
import pandas as pd
import numpy as np
from src.components.data_ingestion import DataIngestion

if __name__=='__main__':
    obj=DataIngestion()
    train_path,test_path=obj.initiate_data_ingestion()
    print(train_path,test_path)