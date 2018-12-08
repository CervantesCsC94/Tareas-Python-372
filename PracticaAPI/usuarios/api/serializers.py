from rest_framework import serializers
from usuarios.models import Usuario



class UsuarioModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Usuario
		fields=[
			"nombre",
			"timestap",
		]
