from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required

app_name="usuarios"

urlpatterns=[

	path('',login_required(views.listUsuarios.as_view()),name="listaUsuarios"),
	path('accounts/login/',LoginView.as_view(template_name='usuario/login.html'),name="login_view"),
	path('logout/',logout_then_login, name='logout'),
]
