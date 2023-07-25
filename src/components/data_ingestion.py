import os,sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import pymongo
import certifi
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from pymongo.mongo_client import MongoClient
ca=certifi.where()

@dataclass
class DataIngestionconfig:
    
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):

        self.data_Ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion is inititated")
            os.makedirs(os.path.dirname(self.data_Ingestion_config.raw_data_path),exist_ok=True)
            uri = "mongodb+srv://abhisheknishad:abhisheknishad@cluster0.rgawbxa.mongodb.net/?retryWrites=true&w=majority"
            client=MongoClient(uri,tlsCAFile=ca)

            DATABASE_NAME="Loan_Defaulter"
            COLLECTION_NAME="loan_data"
            collection=client[DATABASE_NAME][COLLECTION_NAME]
            logging.info("Database and collection is selected")            
            df=pd.DataFrame(list(collection.find()))
            if '_id' in df.columns:
                df=df.drop('_id',axis=1)
            logging.info("Dataframe has been retrieved from MongoDB")

            train_data,test_data=train_test_split(df,test_size=.3,random_state=21)
            df.to_csv(self.data_Ingestion_config.raw_data_path,index=False)
            train_data.to_csv(self.data_Ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.data_Ingestion_config.test_data_path,index=False)
            logging.info("Files is saved in system")

            return(self.data_Ingestion_config.train_data_path,
                    self.data_Ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)
            