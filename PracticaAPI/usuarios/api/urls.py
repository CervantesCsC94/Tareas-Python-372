from django.urls import path
from usuarios.api import views

app_name="api_usuarios"

urlpatterns=[

	path('lista_usuarios/',views.ListUsuariosAPIView.as_view(),name="listAPIView"),
]