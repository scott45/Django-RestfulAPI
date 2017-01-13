from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fellows
from .serializers import FellowsSerializer

# list all fellows or create a new one
# fellow/

class FellowsList(APIView):
    def get(self, request):
        fellows = Fellows.objects.all()
        serializer = FellowsSerializer(fellows, many=True)
        return Response(serializer.data)

    def post(self):
        pass
