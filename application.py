from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import  Predict_data,Customised_Data
from src.logger import logging
from src.exception import CustomException
import os,sys

application=Flask(__name__)
app=application


@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict_default():
    try:
         
        if request.method=='GET':
            return render_template('home.html')
    
        else:
            logging.info("form input is initiated ")
            data=Customised_Data(
                credit_policy=float(request.form['credit policy']),
                purpose=request.form['purpose'],
            
                int_rate=float(request.form['int rate']),
                installment=float(request.form['installment']),
                log_annual_inc=float(request.form['log annual inc']),
                dti=float(request.form['dti']),
                fico=float(request.form['fico']),
                days_with_cr_line=float(request.form['days with cr line']),
                revol_bal=float(request.form['revol bal']),
                revol_util=float(request.form['revol util']),
                inq_last_6mths=float(request.form['inq last 6mths']),
                delinq_2yrs=float(request.form['delinq 2yrs']),
                pub_rec=float(request.form['pub rec']))
            
            logging.info("form input completed")
            df=data.get_dataframe()
            logging.info(f"{df.head()}")
            logging.info("test data is converted into dataframe")
        
            output=Predict_data.predict(df)
            if output==0:
                results='Pay'
            else:
                results='Default'
            return render_template('home.html',results=results)
    except Exception as e:
        logging.info("error occured in processing app through form")
        raise CustomException(e,sys)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)