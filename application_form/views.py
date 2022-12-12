from .models import  Application_form,Alredy_registered_user
from django.http import HttpResponse
from django.shortcuts import render
from application_form.serializers import Application_formSerializer,Alredy_registered_userSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

def application_form(request):
    return render(request,"application_form.html")

def already_registered_user(request):
    return render(request,"already_registered_user.html")


class Application_formView(APIView):
    def post(self, request, format=None):
        serializer = Application_formSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        data = Application_form.objects.all()
        serializer = Application_formSerializer(data, many=True)
        return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)


class Alredy_registered_userView(APIView):
    def post(self, request, format=None):
        serializer = Alredy_registered_userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        data = Alredy_registered_user.objects.all()
        serializer = Alredy_registered_userSerializer(data, many=True)
        return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)