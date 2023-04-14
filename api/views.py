from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from .models import (
    Student,
)

# serializers
from .serializers import (
    StudentSerializer,
)


class StudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk=None) -> Response:
        '''get student'''
        if pk:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    
    def post(self, request: Request) -> Response:
        '''create student'''
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        