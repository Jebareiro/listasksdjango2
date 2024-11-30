from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView

def redirect_to_login(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        return HttpResponseRedirect('/tasks/')  # Si el usuario está autenticado, va a tareas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('', redirect_to_login),  # Redirige a login solo si el usuario no está autenticado
]
