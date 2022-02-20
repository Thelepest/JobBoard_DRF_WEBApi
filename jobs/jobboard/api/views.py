from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response

from jobboard.models import Employee,Joboffer

from jobboard.api.serializers import EmployeeSerializer,JobofferSerializer

"""
CLASS-BASED VIEWS : 3 ENDPOINTS FOR THAT API
"""

class JobofferlistAPIView(APIView):

    """
    Currently active job offer list (READ/POST ONLY). Click on the single offer for details :
    """
    def get(self,request):
        joboffers = Joboffer.objects.filter(active=True)
        serializer = JobofferSerializer(joboffers,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = JobofferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class JobofferdetailAPIView(APIView):

    """
    Selected job offer details. Here, you can both modify and delete it.
    """
    def get_object(self,pk):
        joboffer = get_object_or_404(Joboffer,pk=pk)
        return joboffer

    def get(self,request,pk):
        joboffer = self.get_object(pk)
        serializer = JobofferSerializer(joboffer)
        return Response(serializer.data)

    def put(self,request,pk):
        serializer = JobofferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeelistAPIView(APIView):
    """
    Our employees list (READ/POST ONLY).
    """
    def get(self,request):
        employees = Employee.objects.filter()
        serializer = EmployeeSerializer(employees,many=True,context={"request" : request})
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            