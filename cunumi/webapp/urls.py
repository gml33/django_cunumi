from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register, name='register'),
    path('my-login',views.my_login, name='my-login'),
    path('user-logout',views.user_logout, name='user-logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    #-------------agregar paciente-----------------------------------
    path('crear-paciente', views.agregar_paciente, name='crear-paciente'),
    #modificar paciente-------------------------
    path('modificar-paciente/<int:pk>', views.modificar_paciente, name='modificar-paciente'),
    #detalle paciente-------------------------
    path('detalle-paciente/<int:pk>', views.detalle_paciente, name='detalle-paciente'),
    #eliminar paciente-----------------------------------------------
    path('eliminar-paciente/<int:pk>', views.eliminar_paciente, name='eliminar-paciente'),
]