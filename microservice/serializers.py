from rest_framework import serializers
from .models import Fellows

class FellowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fellows
        fields = '__all__'
