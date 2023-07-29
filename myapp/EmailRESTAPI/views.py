from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import EmailModel
from .Serializer import EmailSerializer

# Create your views here.

# API view for the home page
class HomeView(APIView):
    def get(self, request):
        return Response({'message':'Welcome to RESTFUL API project by Kelvin'})
    

# API view for handling EmailModel instances
class EmailView(APIView):
    # GET request to fetch all EmailModel instances or a specific one by primary key (pk)
    def get(self, request, pk=None):
        if pk:
            try:
                # Fetch the EmailModel instance with the given primary key (pk)
                email_instance = EmailModel.objects.get(pk=pk)
                serializer = EmailSerializer(email_instance)
                return Response(serializer.data)
            except EmailModel.DoesNotExist:
                # If EmailModel instance with the given pk does not exist, return an error message
                return Response({'message':'Email model not found'})
        else:
            # Fetch all EmailModel instances and serialize them to send as a response
            email_instances = EmailModel.objects.all()
            serializer = EmailSerializer(email_instances, many=True)
            return Response(serializer.data)
    
    # POST request to create a new EmailModel instance
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the new EmailModel instance and return its data in the response
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
