from dataclasses import fields
from rest_framework import serializers
from .models import Area, Canal, ClienteCerrado, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Permiso, PermisoArea, Persona, PersonaProyecto, Programmer, Rol, Proyecto



class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'   
        
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'         
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__' 

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__' 

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__' 

class ManzanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzana
        fields = '__all__' 

class PersonaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaProyecto
        fields = '__all__' 

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__' 

class PermisoAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoArea
        fields = '__all__' 

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__' 

class ClienteCerradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteCerrado
        fields = '__all__' 
        
class CronogramaPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronogramaPagos
        fields = '__all__' 

class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = '__all__' 

class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = '__all__' 

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = '__all__' 

class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__' 

class ObservacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observaciones
        fields = '__all__' 