# python segmentation.py --img_path=img_data/crack_segmentation_dataset/train  --prediction_path=figures --classifier_type=R50

import os
import zipfile

os.system("gdown https://drive.google.com/uc?id=1xrOqv0-3uMHjZyEUrerOYiYXW_E8SUMP")

extract_folder_path = "img_data"
path = "crack_segmentation_dataset.zip"

with zipfile.ZipFile(path, 'r') as zip_file:
    zip_file.extractall(extract_folder_path)