import logging
import sys
import os
from datetime import datetime

from src.exception import CustomException

# Step 1: Generate a log file name with a timestamp
# - The filename includes the current date and time in 'MM_DD_YYYY_HH_MM_SS' format.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define the directory to store logs
# - The logs directory is created in the current working directory.
logs_path = os.path.join(os.getcwd(), "logs")  # Create 'logs' directory
os.makedirs(logs_path, exist_ok=True)  # Ensure the directory exists, avoid errors if it already exists

# Step 3: Define the full path for the log file
# - This combines the log directory and the generated log filename.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Configure logging settings
# - Logs will be stored in the specified log file.
# - The format includes timestamp, line number, log level, and message.
# - The logging level is set to INFO to capture general application events.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file location
    format="[ %(asctime)s ] %(lineno)d - %(levelname)s - %(message)s",  # Define log message format
    level=logging.INFO,  # Set logging level to INFO (captures warnings, errors, and critical logs too)
)



if __name__ == "__main__":  # Corrected `__name__` check
    logging.info("Logging has started")
    
    try:
        a = 1/0  # Intentional division by zero
    except Exception as e:
        logging.info("An exception occurred. Logging the error.")
        raise CustomException(str(e), sys)  #  Corrected exception raising
