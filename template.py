# Importing Libraries to create necessary files
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "TextSummarize"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Creating files in the directory
for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(file)

    # Creating Directories
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating Directory {filedir} for the file {filename}.")
    
    # Creating Files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating Empty File: {filepath}.")
    
    else:
        logging.info(f"{filepath} already exists!!!")