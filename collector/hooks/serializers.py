from rest_framework import serializers
from .models import signals
class signalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = signals
        fields = ['id','ticker', 'updated', 'quote','strategy']