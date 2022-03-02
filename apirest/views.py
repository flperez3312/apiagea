import io
import re
import logging
import hdfspackage.hdfsadapter as dfs
from hdfspackage.config import *
from rest_framework.parsers import JSONParser
from django.http import    JsonResponse
from django.views.decorators.csrf import csrf_exempt




logging.basicConfig(level=logging.INFO)
hdfs = dfs.HdfsAdapter(URL, ROOT)
@csrf_exempt
def set_hdfs(request):
  
    if request.method == 'POST':
        
        data = request.body
        stream = io.BytesIO(data)
        dataparse = JSONParser().parse(stream)
        
        try:
           
            regex = r"^/user/[a-zA-Z0-9]{1,}/[a-zA-Z0-9]{1,}[.](txt|csv|json|xml|html|xlsx|xlsdocx|doc|pptx|ppt|pdf|gz|zip|tar|tgz|tbz|avro|orc|parquet|csv|db){1,}$"
            if not re.match(regex, dataparse['path']):

                return JsonResponse({"result": "error path invalido","status":False}, status=400, safe=False)


            if not dataparse['data']:
               
                return JsonResponse({"result":"sin contenido en data","status":False}, status = 400 ,content_type="application/json")
                   
            try:
                if hdfs.file_exists(dataparse['path']):
                    return JsonResponse({"result": "el archivo ya existe","status":False}, status=400, safe=False)
                hdfs.create_file(dataparse['path'], dataparse['data'])

                return JsonResponse({"result":"Archivo creado correctamente","status":True}, status=201, content_type="application/json", safe=False)
               
            except Exception as e:
                return JsonResponse({"result": f"error :{e}","status":False}, status=400, safe=False)
                                  
        except TypeError as e:
            return JsonResponse({"result":f"no se pudo crear el archivo, error: {e}","status":False}, status=400,safe=False)
        except ValueError as e:
            return JsonResponse({"result":f"no se pudo crear el archivo, error: {e}","status":False}, status=400,safe=False)
        
    else:
        return JsonResponse({"result":f"{request.method} no es un metodo valido,  probar con POST","status":False}, status=400, safe=False)
    


@csrf_exempt
def upload_files(request):
    
    if request.method == 'POST':
        data = request.body
        
        stream = io.BytesIO(data)
        dataparse = JSONParser().parse(stream)   
        local_path = dataparse['local_path']
        hdfs_path = dataparse['hdfs_path']
        try:
            if hdfs.upload(hdfs_path, local_path):
                return JsonResponse({"result":"Archivo subido correctamente","status":True},status = 200, content_type="application/json",safe=False)
            else:
                return JsonResponse({"result":"Error: no se pudo subir el archivo", "status": False},status=400, content_type="application/json",safe=False)
        except TypeError as e:
            return JsonResponse({"result":f"no se pudo subir el arcivo, error: {e}","status":False}, status=400, safe=False)

        except Exception as e:
            return JsonResponse({"result":f"no se pudo subir el arcivo, error: {e}","status":False}, status=500, safe=False)
    else:   
        return JsonResponse({"result":f"{request.method} no es un metodo valido,  probar con POST","status":False}, status=400, safe=False)

@csrf_exempt
def hdfs_get_files(request,filename):
   
    if request.method == 'GET':
        
        file_content = None
        try:
            if hdfs.file_exists(f'/user/fperez/{filename}'):
                with hdfs.read_file(f'/user/fperez/{filename}') as f:
                    for line in f:
                        print(line)
                        file_content = str(line.decode('utf-8'))
                        return JsonResponse({"result":file_content,"status":True}, status=200, content_type="application/json",safe=False)
            else:
                return JsonResponse({"result":"Error: no se encontro el archivo","status":False}, status=400, content_type="application/json",safe=False)              
        except TypeError as e:
                return JsonResponse({"result":f"no se pudo leer el arcivo, error: {e}","status":False}, status=400, safe=False)
        except Exception as e:
                return JsonResponse({"result":f"no se pudo leer el arcivo, error: {e}","status":False}, status=500, safe=False)
    
    
    
    if request.method == 'DELETE':
        
        try:
            if hdfs.file_exists(f'/user/fperez/{filename}'):
                hdfs.delete_file(f'/user/fperez/{filename}')
                return JsonResponse({"result":"Archivo eliminado correctamente","status":True}, status=200, content_type="application/json",safe=False)
            else:
                return JsonResponse({"result":"Error: no se encontro el archivo","status":False}, status=400, content_type="application/json",safe=False)
        except TypeError as e:
            return JsonResponse({"result":f"no se pudo eliminar el arcivo, error: {e}","status":False}, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"result":f"no se pudo eliminar el arcivo, error: {e}","status":False}, status=500, safe=False)
    else:
        return JsonResponse({"result":f"{request.method} no es un metodo valido,  probar con GET o DELETE","status":False}, status=400, safe=False, content_type="application/json")




      



         
    




    





        




