from rest_framework import serializers
from escola.models import Estudante, Curso


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']


class CursoSerializer(serializers.ModelField):
    class Meta:
        model = Curso
        fields = '__all__'

