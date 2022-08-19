import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

def list_buckets():
    try:
        buckets = storage_client.list_buckets()
        bucket_list = []
        for bucket in buckets:
            bucket_list.append(str(bucket)) 
        bucket_list = list(map(lambda x: x.replace('<Bucket: ', '').replace('>', ''), bucket_list))
        print(bucket_list)
    except Exception as e:
        print(f'The following exception occurred during the searching process: {e}')


def search_file_in_bucket(bucket_name):
    blob_list = storage_client.list_blobs(bucket_name)
    for blob in blob_list:
        print(blob)
    
    
if __name__ == '__main__':
    list_buckets()
    search_file_in_bucket('bronze-data-storage')
    
