import json 
import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/'

json_data = requests.get(url).json()

#file_names = ['\deputies_data.json', '\deputies_expenses.json']

file_path = r'C:\Users\Vegh\Documents\Estudo\data-pipeline-gcp\src\output_files\deputies_data.json'
file_path_expenses = r'C:\Users\Vegh\Documents\Estudo\data-pipeline-gcp\src\output_files\deputies_expenses.json'

def write_files(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:   
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'The given error occurred while writing file: {e}')
        


if __name__ == '__main__':
    write_files(file_path=file_path)
    write_files(file_path=file_path_expenses)
    
   #for name in file_names: 
        #write_file(file_path=file_path + name)
    








