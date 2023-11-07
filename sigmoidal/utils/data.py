import os
import urllib.request
import zipfile
from pathlib import Path

def download_and_extract_data():
    BUCKET = "my_bucket"
    CODE_FOLDER = Path(".")
    DATA_FILEPATH = CODE_FOLDER / "data" / "data.zip"
    DATA_FOLDER = CODE_FOLDER / "data"
    S3_LOCATION = f"s3://{BUCKET}/penguins"
    
    # Cria a pasta data se não existir
    DATA_FOLDER.mkdir(exist_ok=True)
    
    # Baixa o arquivo zip
    urllib.request.urlretrieve(
        "https://storage.googleapis.com/download.tensorflow.org/data/palmer_penguins/penguins_size.zip", 
        DATA_FILEPATH
    )
    
    # Descompacta o arquivo zip
    with zipfile.ZipFile(DATA_FILEPATH, 'r') as zip_ref:
        zip_ref.extractall(DATA_FOLDER)
