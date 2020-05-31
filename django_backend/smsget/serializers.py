from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PersonInfo



class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonInfo
        fields = ( 
            'num',
            'stat',
            'long',
            'lat',
            'txt',
            'time')
                    
                    
        
        
