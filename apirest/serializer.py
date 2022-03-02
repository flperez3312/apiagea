from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
import logging


class ApiSerializer(serializers.Serializer):
    
    path = serializers.CharField(max_length=1000)
    data = serializers.CharField(max_length=1000)

  
 
   


 
 
    

    
        

    


   

    
   

   
       

    



