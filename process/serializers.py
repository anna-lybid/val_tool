from rest_framework import serializers
from .models import Goal, Product, Contract


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'contract_number', 'financed_amount', 'term', 'balloon', 'monthly_payment', 'annual_irr']