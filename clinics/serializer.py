from rest_framework import serializers
from .models import Clinic


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

    def update(self, instance, validated_data):

        clinic = Clinic.objects.update(**validated_data)
        return clinic



