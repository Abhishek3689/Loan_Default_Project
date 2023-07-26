import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.utils import load_object

class Customised_Data:
     def __init__(self,credit_policy:float,
                    purpose:str,
                    int_rate:float,
                    installment:float,
                    log_annual_inc:float,
                    dti:float,
                    fico:float,
                    days_with_cr_line:float,
                    revol_bal:float,
                    revol_util:float,
                    inq_last_6mths:float,
                    delinq_2yrs:float,
                    pub_rec:float,
     ):
            self.credit_policy=credit_policy,
            self.purpose=purpose,
            self.int_rate=int_rate,
            self.installment=installment,
            self.log_annual_inc=log_annual_inc,
            self.dti=dti,
            self.fico=fico,
            self.days_with_cr_line=days_with_cr_line,
            self.revol_bal=revol_bal,
            self.revol_util=revol_util,
            self.inq_last_6mths=inq_last_6mths,
            self.delinq_2yrs=delinq_2yrs,
            self.pub_rec=pub_rec

     def get_dataframe(self):
        custom_data={'credit.policy':self.credit_policy,
                    'purpose':self.purpose,
                    'int.rate':self.int_rate,
                    'installment':self.installment,
                    'log.annual.inc':self.log_annual_inc,
                    'dti':self.dti,
                    'fico':self.fico,
                    'days.with.cr.line':self.days_with_cr_line,
                    'revol.bal':self.revol_bal,
                    'revol.util':self.revol_util,
                    'inq.last.6mths':self.inq_last_6mths,
                    'delinq.2yrs':self.delinq_2yrs,
                    'pub.rec':self.pub_rec
                    }
        df=pd.DataFrame(custom_data)
        print(df)
        logging.info("Dataframe has been gathered")
        return df


class Predict_data:
    def __init__(self):
        pass

    def predict(features):
        preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
        model_path=os.path.join('artifacts','model.pkl')
       
        preprocessor=load_object(preprocessor_path)
        model=load_object(model_path)
        logging.info("Model and preprocessor has been loaded")
        
        X_scaled=preprocessor.transform(features)
        logging.info("Data has been transformed")
        y_pred=model.predict(X_scaled) 
        logging.info(f"The Result of input paramters is {y_pred[0]}")     
        return y_pred[0]
          