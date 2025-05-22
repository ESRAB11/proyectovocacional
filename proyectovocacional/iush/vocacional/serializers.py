from rest_framework import serializers
from .models import Pregunta

class PreguntaSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    pregunta = serializers.CharField()
    respuestas = serializers.DictField()

    def create(self, validated_data):
        return Pregunta(**validated_data).save()

    def update(self, instance, validated_data):
        instance.pregunta = validated_data.get('pregunta', instance.pregunta)
        instance.respuestas = validated_data.get('respuestas', instance.respuestas)
        instance.save()
        return instance
    
class UsuarioSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    telefono = serializers.CharField(max_length=20)
    carrera_recomendada = serializers.CharField(max_length=100)
    justificacion = serializers.CharField()