import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from src.utils import evaluate_model,save_object
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import sys
import os

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1])

            models={"Logistic Regression":LogisticRegression(),
                "Decision Tree":DecisionTreeClassifier(),
                "Random Forest":RandomForestClassifier(),
                "Ada boost":AdaBoostClassifier(),
                "KNN":KNeighborsClassifier(),
                "SVM":SVC()}
            report=evaluate_model(X_train,y_train,X_test,y_test,models)
            best_score=max(report.values())
            best_model_name=list(report.keys())[list(report.values()).index(best_score)]
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , Accuracy Score : {best_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , Accuracy Score  : {best_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          
            logging.info("best model is saved")
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)