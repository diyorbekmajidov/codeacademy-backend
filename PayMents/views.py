from django.shortcuts import render

from .serializers import PaymentSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.request import Request
from .models import Payment
from datetime import datetime
# import datetime


# Create your views here.
class PaymentView(APIView):
    def post(self, request):
        data = request.data
        d = datetime.strptime(data["start"], '%d/%m/%y')
        e= datetime.strptime(data["end"], '%d/%m/%y')
        myDT = datetime(d.year, d.month, d.day)
        myDT2 = datetime(e.year, e.month, e.day)
        mydata = myDT.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        mydata2 = myDT2.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        data["start"]= mydata
        data["end"]= mydata2
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        payment = Payment.objects.get(id=pk)
        d = datetime.strptime(request.data["start"], '%d/%m/%y')
        e= datetime.strptime(request.data["end"], '%d/%m/%y')
        myDT = datetime(d.year, d.month, d.day)
        myDT2 = datetime(e.year, e.month, e.day)
        mydata = myDT.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        mydata2 = myDT2.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        request.data["start"]= mydata
        request.data["end"]= mydata2
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
class Delet_Payment(APIView):
    def post(self, request, pk):
        try:
            payment = Payment.objects.get(id=pk)
            payment.delete()
            return Response("Payment Deleted")
        except:
            return Response("Payment Not Found")
        
        
    

        

