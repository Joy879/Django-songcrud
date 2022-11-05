from . models import Song, Artiste
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_released = validated_data.get('date_released', instance.date_released)
        instance.save()
        return instance
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"