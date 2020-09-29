from rest_framework import serializers

from .models import Netflix

class NetflixSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','user','series', 'movie', 'episode', 'season')
        model = Netflix