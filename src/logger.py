import logging
import os
import sys
from datetime import datetime

log_file=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)

log_file_path=os.path.join(logs_path,log_file)

logging.basicConfig(filename=log_file_path,level=logging.INFO,format="[ %(asctime)s] %(lineno)d %(name)s -%(levelname)s-%(message)s")