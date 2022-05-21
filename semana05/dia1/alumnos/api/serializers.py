from rest_framework import serializers

from .models import Alumno,Profesor

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()
    
    def create(self, validated_data):
        return Alumno.objects.create(**validated_data)
 
 ####ESTO COGE TODOS LOS CAMPOS DE LA TABLA PROFESOR SIN SEPARAR COMO LIENAS ARRIBAS   
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'