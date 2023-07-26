# from src.components.data_ingestion import DataIngestion
# dataingestion=DataIngestion()
# train_path,test_path=dataingestion.initiate_data_ingestion()

# from src.components.data_transformation import DataTransformation
# data_transformation=DataTransformation()
# train_arr,test_arr=data_transformation.initiate_data_transformation(train_path,test_path)

# from src.components.model_trainer import ModelTrainer
# modeltrainer=ModelTrainer()
# modeltrainer.initate_model_training(train_arr,test_arr)

from src.pipelines.prediction_pipeline import Customised_Data,Predict_data
customdata=Customised_Data(1,'credit_card',.11,829,12,19,767,6000,28854,54,0,0,0)
df=customdata.get_dataframe()
y_pred=Predict_data.predict(df)
print(y_pred)