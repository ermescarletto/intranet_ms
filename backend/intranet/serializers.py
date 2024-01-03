from rest_framework import serializers
from .models import Unidade, Departamento, Cargo, PerfilColaborador, Comunicados, EnviosComunicados, MeusComunicados

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class PerfilColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilColaborador
        fields = '__all__'

class ComunicadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicados
        fields = '__all__'

class EnviosComunicadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnviosComunicados
        fields = '__all__'

class MeusComunicadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeusComunicados
        fields = '__all__'