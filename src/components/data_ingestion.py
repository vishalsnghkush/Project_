import sys
import os
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import logging
import pandas as pd

@dataclass
class Data_Ingestion_Config:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")



class Data_Ingestion:
    def __init__(self):
        self.ingestion_config=Data_Ingestion_Config()
    
    def initiate_data_ingestion(self):
        logging.info("Ingection get started")

        try:
            logging.info("Loading of Data Started ")
            df=pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Data Read as DataFrame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=Data_Ingestion()
    train_data,test_data=obj.initiate_data_ingestion()