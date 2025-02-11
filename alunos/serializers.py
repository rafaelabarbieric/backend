from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Estado 
from .models import Cidade
from .models import Pessoa

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'