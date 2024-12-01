from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Ruta para registrarse y loguearse a la vez, usando una vista personalizada
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'), 

    # Ruta para iniciar sesión (login)
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,  # Si el usuario ya está autenticado, lo redirige
        template_name='accounts/login.html'  # Template de login personalizado
    ), name='login'),

    # Ruta para iniciar sesión (signin) - Esto parece ser lo mismo que la ruta de login, ¿debería ser igual?
    path('signin/', LoginView.as_view(
        redirect_authenticated_user=True, 
        template_name='accounts/login.html'
    ), name='signin'),

    # Ruta para cerrar sesión (logout)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Ruta para ver los detalles del usuario (puedes poner un nombre más claro si lo prefieres)
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    # Ruta para actualizar los detalles del usuario
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),

    # Ruta para cambiar la contraseña del usuario
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),

    # Ruta que muestra que el cambio de contraseña fue exitoso
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),

    # Ruta para eliminar un usuario (este es un caso delicado, asegúrate de que sólo los admin puedan hacer esto)
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
]