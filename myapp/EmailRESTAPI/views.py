from django.shortcuts import render
from django.shortcuts import get_object_or_404


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import EmailModel
from .Serializer import EmailSerializer





# Create your views here.
class HomeView(APIView):
    def get(self, request):
        return Response({'message':'Welcome to RESTFUL API project by Kelvin'})
    

    
class EmailView(APIView):
    def get(self, request,pk=None):
        if pk:
            try:
                EmailView= EmailModel.objects.get(pk=pk)
                serializer= EmailSerializer(EmailView)
                return Response(serializer.data)
            except EmailModel.DoesNotExist:
                return Response({'message':'Email model not found'})
        else:
            EmailView=EmailModel.objects.all()
            serializer=EmailSerializer(EmailView,many=True)
            return Response(serializer.data)
    
    def post(self,request):
        serializer=EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def get_authenticate_header(self, request):
        return super().get_authenticate_header(request)
    