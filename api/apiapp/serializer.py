from rest_framework import serializers
from .models import travels

class tserial(serializers.ModelSerializer):
    class Meta:
        model=travels
        fields='__all__'
        
        
        