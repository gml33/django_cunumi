from .models import paciente
from rest_framework import serializers


class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=paciente
        fields = '__all__'