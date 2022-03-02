import hdfsadapter as hdfs
from   hdfs import *
from config import *
from django.test import TestCase

# Create your tests here.

class HdfsAdapterTest(TestCase):
    def test_hdfs_adapter(self):
        hdfs_adapter = hdfs.HdfsAdapter(URL, ROOT)
        hdfs_adapter.create_file("/user/fperez/prueba.txt","/user/fperez/" )
        content = hdfs_adapter.read_file("/user/fperez/prueba.txt")
        print(content)  # b'Hello World!'
     




if __name__ == '__main__':

    
    #test_hdfs_adapter = HdfsAdapterTest()
    #test_hdfs_adapter.test_hdfs_adapter()

    hdfss = hdfs.HdfsAdapter(URL, ROOT)
    
    
    #print(cliente.list_dir_files("/user/fperez/"))
    #print(cliente.read_file('/user/fperez/'))
    
    """
    
    if hdfss.list_dir_files('/user/fperez'):
        
        print("Existe")
    else:

        print(hdfss.list_dir_files('/user/fperez'))
    

    """

    
    #print(cliente.list_files())
  
    #print(cliente.list_dir_files('/user/fperez/'))

    

    