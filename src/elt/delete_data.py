import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

bucket_name = 'bronze-data-storage'

files_to_delete = ['deputies_list', 'deputies_expenses']

def delete_files_from_bucket(bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        for file in files_to_delete:
            blob = bucket.blob(file)
            blob.delete()
    except Exception as e:
        print(f'The given error occurred during the delete process: {e}')
  
    
if __name__ == '__main__':
    delete_files_from_bucket(bucket_name)    
        
        
    