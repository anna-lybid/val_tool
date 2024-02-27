from rest_framework import serializers
from process.models import Bus, Product


class ProcessSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    info = serializers.CharField(required=False)
    num_seat = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Bus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.info = validated_data.get('info', instance.info)
        instance.num_seat = validated_data.get('num_seat', instance.num_seat)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # info = serializers.CharField(required=False)
    # formula = serializers.CharField(required=True)
    #
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.info = validated_data.get('info', instance.info)
    #     instance.formula = validated_data.get('formula', instance.formula)
    #     instance.save()
    #     return instance
    class Meta:
        model = Product
        fields = '__all__'

