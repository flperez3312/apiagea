from distutils.command.upload import upload
from django.urls import path,re_path
from .views import set_hdfs,upload_files,hdfs_get_files

# Create your views here.



urlpatterns = [
    path('hdfs_files', set_hdfs),
    path('hdfs_from_local', upload_files),
    re_path('hdfs_file/(?P<filename>[\w\d\_\-\.]+\.[\w\d\_\-\.]+)$', hdfs_get_files),
    

]