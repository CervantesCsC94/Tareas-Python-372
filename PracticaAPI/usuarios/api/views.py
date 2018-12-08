from rest_framework import generics
from usuarios.api.serializers import UsuarioModelSerializer
from usuarios.models import Usuario


class ListUsuariosAPIView(generics.ListAPIView):
	serializer_class=UsuarioModelSerializer

	def get_queryset(self, *args,**kwargs):
		return Usuario.objects.all()