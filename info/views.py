from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import InformationSerializer




@api_view(['POST'])
@permission_classes((AllowAny, ))
def post_info(request) :
    ser = InformationSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else :
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)