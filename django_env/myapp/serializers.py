from rest_framework import serializers
from .models import Pet, Specie

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    # especie = EspecieSerializer()

    class Meta:
        model = Pet
        fields = '__all__'