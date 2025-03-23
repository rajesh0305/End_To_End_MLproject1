import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
from src.exception import CustomException
from src.logger import Logger
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
  train_data_path: str=os.path.join('artifacts','data','train_data.csv')
  test_data_path: str=os.path.join('artifacts','data','test_data.csv')
  raw_data_path: str=os.path.join('artifacts','data','raw_data.csv')
  
    
class DataIngestion:
  def __init__(self):
    self.injection_config = DataIngestionConfig()
    
  def initiate_data_ingestion(self):
    Logger.info("Entered the data ingestion method or component")
    try:
      df = pd.read_csv('notebook\data\stud.csv')
      Logger.info("Read the data from the dataframe")
      
      os.makedirs(os.path.dirname(self.injection_config.train_data_path), exist_ok=True)
      
      df.to_csv(self.injection_config.train_data_path, index=False, header=True)
      
      Logger.info("Train data saved successfully")
      train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
      
      train_set.to_csv(self.injection_config.train_data_path, index=False, header=True)
      
      test_set.to_csv(self.injection_config.test_data_path, index=False, header=True)
      
      Logger.info("Ingestion of the data completed successfully")
      
      return (
          self.injection_config.train_data_path,
          self.injection_config.test_data_path
      )
      
    except Exception as e:
      Logger.error(f"Error during data ingestion: {e}")
      raise CustomException(e, sys)
      
  if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()