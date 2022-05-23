from rest_framework import serializers

from quad_dj_app.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
