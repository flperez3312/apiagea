from django.test import TestCase
import json
import asyncio
import time
import requests

from concurrent.futures import ThreadPoolExecutor
# Create your tests here.

class TestApi(TestCase):
    def test_set_hdfs(self):
        
        url = 'http://127.0.0.1:8000/apiagea/v1/hdfs_files'
     
        data = {

            "path": "/user/fperez/prueba.txt",
            "data": "hola mundo"
        }
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Archivo creado correctamente')
   
        data = {'path':'/user/fperez/testeo.txt','data':'Hello World!'}
    
   
        r = requests.post(url, json=data)
    
        r = requests.get(url)
        print(r.text)

    def test_hdfs_files(self):
        url = 'http://127.0.0.1:8000/apiagea/v1/hdfs_file'
        data = {'filename':'prueba.txt'}
        r = requests.get(url, params=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['message'], 'Archivo encontrado')
        self.assertEqual(r.json()['data'], 'hola mundo')

    def test_upload_files(self):
        url = 'http://127.0.0.1:8000/apiagea/v1/hdfs_from_local'
        data = {'local_path':'prueba.txt','hdfs_path':'/user/fperez/prueba.txt'}
        r = requests.post(url, json=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['message'], 'Archivo creado correctamente')

    def test_delete_files(self):
        url = 'http://127.0.0.1:8000/apiagea/v1/hdfs_file'
        data = {'filename':'prueba.txt'}
        r = requests.delete(url, params=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['message'], 'Archivo eliminado')








_executor = ThreadPoolExecutor(1)


def sync_blocking():
    time.sleep(1)





async def fetch_data():
    print('start fetching')
    url = 'http://127.0.0.1:8000/apiagea/v1/hdfs_files'
    headers = {'Content-Type': 'application/json'}
    for i in range(100, 120):
        data = {'path': f'/user/fperez/test{str(i)}file.txt' , 'data': f'test_file{str(i)}.txt'}
        await loop.run_in_executor(_executor, sync_blocking)
        res = requests.post(url, data=json.dumps(data), headers=headers)
        print(res.status_code)
        print(res.text)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_data())
loop.close()

    
    

#python3 manage.py test apirest.tests.TestApi
#python3 manage.py test apirest.tests.TestApi.test_api_save
#python3 manage.py test apirest.tests.TestApi.test_api_save --keepdb


