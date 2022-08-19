## Introduction

    The main purpose of this project is to create a complete yet simple data pipeline, including ETL, data analysis and DataViz, using technologies as Python, Google Cloud Platform, Jupyter and PowerBI.

    Initially the project is being built only in Python, but I have the intention of upgrade the pipeline using technologies like Airflow, Prefect, Great Expectations, Spark(PySpark) and others while I'm learning and improving my actual hard skills.

    The API used in this project is the Brazilian Camara dos Deputados(Chamber of Deputies) Open Data API, and it can be found in this link: https://dadosabertos.camara.leg.br/swagger/api.html#api. This API provides a huge amount of data about Brazil's deputies, and the data used in this project are those of parliamentary expenses.

## Technologies
     - Python
     - PowerBI
     - Google Cloud Storage
     - Jupyter Notebook
     - APIRestful
     - Json

## References
    Until now, the references used in this project are:
        - https://learndataanalysis.org/source-code-using-google-cloud-storage-api-in-python-for-beginners/
        - https://understandingdata.com/how-to-clean-and-process-data/
  
## Next steps
    - Create function to delete files in the bucket. (OK)
    - Create function to search among the buckets
    - Upgrade write_file and upload_file_to_bucket functions to work regardless of the number of files to be writem and uploaded.
    - Maybe create a class to abstract all functions created would be nice
    - Data quality and data transformation
    - Dataviz

  


