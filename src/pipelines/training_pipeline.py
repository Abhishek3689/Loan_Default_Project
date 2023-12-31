import os,sys
import pandas as pd
import numpy as np
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


dataingestion=DataIngestion()
train_path,test_path=dataingestion.initiate_data_ingestion()
#print(train_path,test_path)

data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initiate_data_transformation(train_path,test_path)

modeltrainer=ModelTrainer()
modeltrainer.initate_model_training(train_arr,test_arr)