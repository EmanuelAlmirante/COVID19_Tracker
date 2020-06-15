from rest_framework import serializers
from covid_tracker_backend.models import COVIDData


class COVIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = COVIDData
        fields = ('id',
                  'country',
                  'total_cases',
                  'new_cases',
                  'total_deaths',
                  'new_deaths',
                  'total_recovered',
                  'active_cases',
                  'day')
