from datetime import datetime
import logging
from operator import le
from hdfs import *
from hdfs.util import *
from hdfs.util import HdfsError

logging.basicConfig(level=logging.DEBUG)

class HdfsAdapter:
    

    
    def __init__(self, url, user):
        
        self.url = url
        self.user = user
        self.cliente = InsecureClient(self.url, user=self.user)
        logging.info(f"HdfsAdapter task started {datetime.now()}")
        
        

    @property
    def exists(self):
        try:
            self.cliente.status("/")
            logging.info("Connection established")
            return True
                
        except HdfsError and ConnectionError as e:
            logging.error("Error creating HdfsAdapter: %s", e)
            return False
            
    
    def create_file(self, filename, content):
        try:
            self.cliente.write(filename, content)
            logging.info("File created")
            return True
        except HdfsError as e:
            logging.error("Error creating file: %s", e)
            return False
    
 
    def read_file(self, filename):
        try:
            content = self.cliente.read(filename, length=None)
            logging.info("File read")
            return content
        except HdfsError as e:
            logging.error("Error reading file: %s", e)
            return False
    
    @property
    def list_dir(self):
        try:
            list_dir = self.cliente.list('.')

            logging.info("List dir")
            return list_dir
        except HdfsError as e:
            logging.error("Error listing dir: %s", e)
            return False

    
    def list_dir_files(self, dir):
        try:
            list_dir_files = self.cliente.list(dir)

            logging.info("List dir files")
            return list_dir_files
        except HdfsError as e:
            logging.error("Error listing dir files: %s", e)
            return False

    
    def file_exists(self, filename):
        try:
            self.cliente.status(filename)
            logging.info("File exists")
            return True
        except HdfsError as e:
            logging.error("Error checking file exists: %s", e)
            return False
   
  
    def delete_file(self, filename):
        try:
            self.cliente.delete(filename)
            logging.info("File deleted")
            return True
        except HdfsError as e:
            logging.error("Error deleting file: %s", e)
            return False
    
   
    def upload(self, hdfs_path, local_path):
        try:
            self.cliente.upload(hdfs_path=hdfs_path, local_path=local_path)
            logging.info("File uploaded")
            return True
        except HdfsError as e:
            logging.error("Error uploading file: %s", e)
            return False


    def __del__(self):
        logging.info(f"HdfsAdapter task completed {datetime.now()}")



        
    

            
        



    


    



    

    


    
 
    

