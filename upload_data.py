from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import certifi

ca = certifi.where()
# uniform resource indentifier
uri =  "mongodb+srv://abhisheknishad:abhisheknishad@cluster0.rgawbxa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# create database name and collection name
DATABASE_NAME="Loan_Defaulter"
COLLECTION_NAME="loan_data"

# read the data as a dataframe
df=pd.read_csv("https://raw.githubusercontent.com/Abhishek3689/Test_Train_Datsets_CSV_Excel/main/loan_borowwer_data.csv")
#df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)