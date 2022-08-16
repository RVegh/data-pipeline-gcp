import os
from extract_data import file_path, file_path_expenses
from google.cloud import storage

#Google Cloud json managed key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

bucket_name = 'bronze-data-storage'

def upload_files_to_bucket(blob_name, file_path, bucket_name):
      try:
          bucket = storage_client.get_bucket(bucket_name)
          blob = bucket.blob(blob_name)
          blob.upload_from_filename(file_path)
      except Exception as e:
          print(f'The given error occurred during the upload: {e}')


if __name__ == '__main__':
    upload_files_to_bucket('deputies_list', file_path=file_path, bucket_name=bucket_name)
    upload_files_to_bucket('deputies_expenses', file_path=file_path_expenses, bucket_name=bucket_name)             
    
    

