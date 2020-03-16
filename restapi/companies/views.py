
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stock
from .serializers import StockSerializer
# Create your views here.

class StockList(APIView):

    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks,many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass