import os 
import requests
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

bucket_name = 'bronze-data-storage'

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

json = requests.get(url).json()

print(json)







