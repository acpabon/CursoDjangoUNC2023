from rest_framework import serializers
from .models import Mascot, Specie, Observation

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascot
        fields = '__all__'

class ObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'
