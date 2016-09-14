from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clinic
from .serializer import ClinicSerializer

# Create your views here.


class ClinicList(APIView):

    def get(self,request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response({'results': serializer.data})

    def post(self, request):

        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():

            serializer.update(Clinic, serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

