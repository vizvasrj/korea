from rest_framework import serializers

class KonlpySerializer(serializers.Serializer):
    text = serializers.CharField()

