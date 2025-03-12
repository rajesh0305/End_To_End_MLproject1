import logging
import os
from datetime import datetime

# Define log file name
LOG_FILE = f"{datetime.now().strftime('%y-%m-%d')}.log"

# Define log directory
logs_path = os.path.join(os.getcwd(), "logs")

# Create directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__=="__main__":
  logging.info("logging has been configured successfully")