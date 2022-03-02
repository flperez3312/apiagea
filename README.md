__AGEA INGESTA API PROJECT__



1 *API_Ingesta es un proyecto que se ira escalando una vez que este aprobados los cambios desde la rama develop; para hacer pruebas intenta esto en bash/terminal*:

>git clone https://github.com/flperez3312/apiagea.git
>
>cd apiagea
>
>pip install virtualenv(si ya lo tenes no lo agregues...)
>
>pip install -r requirements

2 *Recorda modificar tu archivo config con los datos de tu HOSTNAME Y ROOT*

```JSON
URL = 'HOSTNAME'
ROOT ='USERNAME'
```

### *Test para crear archivos nuevos*
- *POST {hostname}/apiagea/v1/hdfs_files*
- Content-Type: application/json
```JSON
{
    "path": "/user/<tu nombre>/<nombre del archivo con extension",
    "data": "contenido del archivo puede ser texto json, etc"
    
}
```
*response*
        
```JSON
{
    "result": "Archivo creado correctamente",
    "status": "true"
    
}
```
*errors*
        
- path error
        
```JSON
{
    "result": "error path invalido",
    "status": "false"
    
}
```
*ejemplo  error en key 'data'*
        
```JSON
{
    "result": "no se pudo crear el archivo, error: 'int' object is not iterable ",
    "status": "false"
    
}
```
        
### la api valida y captura los errors mostrando una respuesta status false con el estado del error


- Script de prueba pegarle a la api que ingesta en archivos nuevos al directorio(este es un ejemplo y se puede hacer de muchas maneras) 
 
      
```PYTHON

_executor = ThreadPoolExecutor(1)


def sync_blocking():
    time.sleep(1)





async def fetch_data():
    print('start fetching')
    url = '<hostname>/apiagea/v1/hdfs_files'
    headers = {'Content-Type': 'application/json'}
    for i in range(100, 120):
        data = {'path': f'/user/<usuario>/test{str(i)}file.txt' , 'data': f'test_file{str(i)}.txt'}
        await loop.run_in_executor(_executor, sync_blocking)
        res = requests.post(url, data=json.dumps(data), headers=headers)
        print(res.status_code)
        print(res.text)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_data())
loop.close()

```
        
**Copia archivos de ti directorio a el cluster**
        
      
_**POST <hostname>/apiagea/v1/hdfs_from_local**
      
      


  
