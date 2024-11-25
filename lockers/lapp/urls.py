from django.urls import path
from . import views

urlpatterns = [
    #path('usuarios/', views.usuarios_list, name='usuarios_list'),
    #path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),
    #path('usuarios/<int:usuario_id>/editar/', views.usuario_update, name='usuaVrio_update'),
    #path('usuarios/<int:usuario_id>/eliminar/', views.usuario_delete, name='usuario_delete'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', views.password_change, name='password_change'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('casilleros', views.casilleros_list, name='casilleros_list'),
    path('', views.home, name='home'),
    path('casilleros/<int:casillero_id>/', views.casillero_detail, name='locker_detail'),  # Detalles del casillero
]
