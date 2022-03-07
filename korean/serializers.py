from rest_framework import serializers

class KonlpySerializer(serializers.Serializer):
    name = serializers.CharField()

