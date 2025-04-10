#this is related to read data 
import os
import sys
from src.exception_01 import CustomException  
from src.logger_02 import logging 
import pandas as pd  
  

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # for creating classes with default values

@dataclass 
class DataIngestionConfig:  #which is used to create a class with default values
    """
    Configuration class for data ingestion.
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
    
class DataIngestion:
    """
    Class for data ingestion.
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Initialize the config class

    def initiate_data_ingestion(self):
        """
        Method to initiate data ingestion.
        """
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("Notebook\data\student_data.csv") 
            
 #read the data from csv file
            logging.info("Read the dataset as dataframe")
            
            
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # Create directories if they don't exist
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  # Save the raw data
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  # Split the data into train and test sets
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)  # Save the train set
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  # Save the test set
            logging.info("Ingestion of data is completed")
            
            return (self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path,
                )  # Return the paths of the train and test sets
            
            
        except Exception as e:
            
            # logging.info("Exception occurred at data ingestion stage")
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()