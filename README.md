__AGEA INGESTA API PROJECT__



1 *API_Ingesta es un proyecto que se ira escalando aprobando  los pull request desde la rama develop; para realizar  pruebas intenta esto en bash/terminal*:

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
- *POST {HOSTNAME}/apiagea/v1/hdfs_files*
- Content-Type: application/json
```JSON
{
    "path": "/user/{usuario}/{nombre del archivo con extension}",
    "data": "contenido del archivo puede ser texto json, etc"
    
}
```
*response*
        
```JSON
{
    "result": "Archivo creado correctamente",
    "status": true
    
}
```
*errors*
        
- path error
        
```JSON
{
    "result": "error path invalido",
    "status": false
    
}
```
*ejemplo  error en key 'data'*
        
```JSON
{
    "result": "no se pudo crear el archivo, error: 'int' object is not iterable ",
    "status": false
    
}
```
        
### la api valida y captura los errors mostrando una respuesta status false con el estado del error


- ejemplo de un script  en python  para crear archivos....
      
```PYTHON

_executor = ThreadPoolExecutor(1)


def sync_blocking():
    time.sleep(1)





async def fetch_data():
    print('start fetching')
    url = '{HOSTNAME}/apiagea/v1/hdfs_files'
    headers = {'Content-Type': 'application/json'}
    for i in range(100, 120):
        data = {'path': f'/user/{usuario}/test{str(i)}file.txt' , 'data': f'test_file{str(i)}.txt'}
        await loop.run_in_executor(_executor, sync_blocking)
        res = requests.post(url, data=json.dumps(data), headers=headers)
        print(res.status_code)
        print(res.text)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_data())
loop.close()

```
        
**Copia archivos de ti directorio a el cluster**
        
      
- *POST {HOSTNAME}/apiagea/v1/hdfs_from_local*

- Content-Type: application/json
```JSON
{
    "local_path": "{ruta de tu archivo local:ejemplo:(c:/Users/usuario/documentos/archivoprueba.txt)}",
    "hdfs_path": "/user/{tu usuario}"
    
}
```

*response*

```JSON
{
    "result": "Archivo creado correctamente",
    "status": true
    
}
```

**Ver contenido de un archivo
- *GET {HOSTNAME}/apiagea/v1/hdfs_file/{NOMBRE_DEL_ARCHIVO_CON_EXTENSION}*

*response*

```JSON
{
    "result": "CONTENIDO DEL ARCHIVO",
    "status": true
    
}
```
      
      
 **Eliminar un archivo
- *DELETE {HOSTNAME}/apiagea/v1/hdfs_file/{NOMBRE_DEL_ARCHIVO_CON_EXTENSION}*

*response*

```JSON
{
    "result": "Archivo eliminado",
    "status": true
    
}
```
    


  
