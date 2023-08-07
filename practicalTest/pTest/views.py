from urllib import response
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from pTest.models import Test
from pTest.serializers import Testserializer

# Create your views here.
@api_view(['GET'])
def msg(request):
    return Response("Hello, Welcome to the backend practical test!")


@api_view(['POST'])
def insertTest(request):
    serializer = Testserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getTest(request):
    test = Test.objects.all()
    serializer = Testserializer(test, many=True)
    return Response(serializer.data)



