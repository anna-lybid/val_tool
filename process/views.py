import csv

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goal, Product, Contract
from .serializers import GoalSerializer, ProductSerializer, ContractSerializer


class GoalListCreate(generics.ListAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContractUploadView(APIView):
    template_name = 'upload_file.html'
    def post(self, request, format=None):
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        csv_file = request.FILES['file']
        contracts_created = []

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                serializer = ContractSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
                    contracts_created.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(contracts_created, status=status.HTTP_201_CREATED)
