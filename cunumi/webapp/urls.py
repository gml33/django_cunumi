from django.urls import path, include
from . import views
from .views import pacienteViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('paciente', pacienteViewset)


urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register, name='register'),
    path('my-login',views.my_login, name='my-login'),
    path('user-logout',views.user_logout, name='user-logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    #------------------------paciente--------------------------------
    path('agregar-paciente', views.agregar_paciente, name='agregar_paciente'),
    path('detalle-paciente/<int:pk>', views.detalle_paciente, name='detalle_paciente'),
    path('eliminar-paciente/<int:pk>', views.eliminar_paciente, name='eliminar_paciente'),
    path('modificar-paciente/<int:pk>', views.modificar_paciente, name='modificar_paciente'),

    # -----------------------derivaciones---------------------------------
    path('agregar-derivacion/',  views.agregar_derivacion, name='agregar_derivacion'),
    path('detalle-derivacion/<id>/',  views.detalle_derivacion, name='detalle_derivacion'),
    path('listar-derivacion/',  views.listar_derivaciones, name='listar_derivaciones'),
    path('modificar-derivacion/<id>/', views.modificar_derivacion, name='modificar_derivacion'),
    path('eliminar-derivacion/<id>/', views.eliminar_derivacion, name='eliminar_derivacion'),
        # -----------------------evoluciones-----------------------------
    path('agregar-evolucion/',  views.agregar_evolucion, name='agregar_evolucion'),
    path('detalle-evolucion/<id>/',  views.detalle_evolucion, name='detalle_evolucion'),
    path('listar-evoluciones/',  views.listar_evoluciones, name='listar_evoluciones'),
    path('modificar-evolucion/<id>/', views.modificar_evolucion, name='modificar_evolucion'),
    path('eliminar-evolucion/<id>/',  views.eliminar_evolucion, name='eliminar_evolucion'),
    #-------------------------historiasClinicas------------------------
    path('agregar-historiaClinica/', views.agregar_historiaClinica,name='agregar_historiaClinica'),
    path('detalle-historiaClinica/<id>/', views.detalle_historiaClinica, name='detalle_historiaClinica'),
    path('listar-historiasClinicas/',  views.listar_historiasClinicas, name='listar_historiasClinicas'),
    path('modificar-historiaClinica/<id>/', views.modificar_historiaClinica, name='modificar_historiaClinica'),
    path('eliminar-historiaClinica/<id>/', views.eliminar_historiaClinica, name='eliminar_historiaClinica'),
    #-------------------------facturas------------------------
    path('agregar-factura/', views.agregar_factura,name='agregar_factura'),
    path('detalle-factura/<id>/', views.detalle_factura, name='detalle_factura'),
    path('listar-facturas/',  views.listar_facturas, name='listar_facturas'),
    path('modificar-factura/<id>/', views.modificar_factura, name='modificar_factura'),
    path('eliminar-factura/<id>/', views.eliminar_factura, name='eliminar_factura'),
    #-------------------------turnos------------------------
    path('agregar-turno/', views.agregar_turno,name='agregar_turno'),
    path('detalle-turno/<id>/', views.detalle_turno, name='detalle_turno'),
    path('listar-turnos/',  views.listar_turnos, name='listar_turnos'),
    path('modificar-turno/<id>/', views.modificar_turno, name='modificar_turno'),
    path('eliminar-turno/<id>/', views.eliminar_turno, name='eliminar_turno'),
    #------------------------API-----------------------------
    path('api/v1/', include(router.urls))
    ]