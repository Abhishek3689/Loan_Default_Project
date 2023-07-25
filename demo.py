from src.components.data_ingestion import DataIngestion
dataingestion=DataIngestion()
train_path,test_path=dataingestion.initiate_data_ingestion()

from src.components.data_transformation import DataTransformation
data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initiate_data_transformation(train_path,test_path)

from src.components.model_trainer import ModelTrainer
modeltrainer=ModelTrainer()
modeltrainer.initate_model_training(train_arr,test_arr)