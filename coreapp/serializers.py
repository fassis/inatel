from rest_framework import serializers

from coreapp.models import HealthUnity, HealthUnityFile

class HealthUnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthUnity
        fields = ['cnes_code', 'ibge_uf', 'ibge_city',
                 'name', 'address', 'district', 'lat',
                 'lon', 'file', 'created_at'
                 ]
        depth = 1