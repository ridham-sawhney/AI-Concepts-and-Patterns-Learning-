import os
import logging

def Logger(project_name):
    # 1. Get the path to Logger.py
    current_file_path = os.path.abspath(__file__)
    
    # 2. Go up one level to RSYLogger/, then another level to project_root/
    project_root = os.path.dirname(os.path.dirname(current_file_path))
    
    # 3. Define the sibling folder name (e.g., "project_logs")
    log_dir = os.path.join(project_root, "logs")
    
    # 4. Create the folder if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 5. Define the full .txt file path
    log_file_path = os.path.join(log_dir, f"{project_name}.txt")
    
    # 6. Setup the standard Python logger
    logger = logging.getLogger(project_name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # mode='a' ensures it keeps appending to the .txt file
        handler = logging.FileHandler(log_file_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

# Usage
# log = Logger("MyProjectName")
# log.info("Appending data to sibling folder...")
