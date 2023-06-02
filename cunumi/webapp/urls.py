from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register, name='register'),
    path('my-login',views.my_login, name='my-login'),
    path('user-logout',views.user_logout, name='user-logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    #------------------------paciente--------------------------------
    path('crear-paciente', views.agregar_paciente, name='crear-paciente'),
    path('eliminar-paciente/<int:pk>', views.eliminar_paciente, name='eliminar-paciente'),
    path('modificar-paciente/<int:pk>', views.modificar_paciente, name='modificar-paciente'),
    path('detalle-paciente/<int:pk>', views.detalle_paciente, name='detalle-paciente'),
    #------------------------paciente--------------------------------# ------------historiaClinicas----------------------------
    path('agregar-historiaClinica/', views.agregar_historiaClinica,name='agregar_historiaClinica'),
    path('detalle-historiaClinica/<id>/', views.detalle_historiaClinica, name='detalle_historiaClinica'),
    path('listar-historiaClinicas/',  views.listar_historiaClinicas, name='listar_historiaClinicas'),
    path('modificar-historiaClinica/<id>/', views.modificar_historiaClinica, name='modificar_historiaClinica'),
    path('eliminar-historiaClinica/<id>/', views.eliminar_historiaClinica, name='eliminar_historiaClinica'),
    # ------------evoluciones----------------------------
    path('agregar-evolucion/',  views.agregar_evolucion, name='agregar_evolucion'),
    path('detalle-evolucion/<id>/',  views.detalle_evolucion, name='detalle_evolucion'),
    path('listar-evoluciones/',  views.listar_evoluciones, name='listar_evoluciones'),
    path('modificar-evolucion/<id>/', views.modificar_evolucion, name='modificar_evolucion'),
    path('eliminar-evolucion/<id>/',  views.eliminar_evolucion, name='eliminar_evolucion'),
    # -----------------------derivaciones---------------------------------
    path('agregar-derivacion/',  views.agregar_derivacion, name='agregar_derivacion'),
    path('detalle-derivacion/<id>/',  views.detalle_derivacion, name='detalle_derivacion'),
    path('listar-derivacion/',  views.listar_derivaciones, name='listar_derivaciones'),
    path('modificar-derivacion/<id>/', views.modificar_derivacion, name='modificar_derivacion'),
    path('eliminar-derivacion/<id>/', views.eliminar_derivacion, name='eliminar_derivacion'),]