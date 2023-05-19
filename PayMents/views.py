from django.shortcuts import render

from .serializers import PaymentSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.request import Request
from .models import Payment


# Create your views here.
class PaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

