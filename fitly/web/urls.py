
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path("", views.index_view, name='index'),
    path("login/", views.login_view, name='index'),
    path("registro/", views.signup_view, name='index'),

    path("clases/", views.clases_view, name='clases'),
    path("confirmacion-contrato/", views.confirmacionContrato_view, name='confirmacion-contrato'),
    path("confirmacion-recuperar/", views.confirmacionRecuperar_view, name='confirmacion-recuperar'),
    path("contacto/", views.contacto_view, name='contacto'),
    path("contratar-avanzado/", views.contratarAvanzado_view, name='contratar-avanzado'),
    path("contratar-basico/", views.contratarBasico_view, name='contratar-basico'),
    path("contratar-premium/", views.contratarPremium_view, name='contratar-premium'),
    path("instalaciones/", views.instalaciones_view, name='instalaciones'),
    path("recuperar-contraseña/", views.recuperarContraseña_view, name='recuperar-contraseña'),
    path("tarifas/", views.tarifas_view, name='tarifas'),

]
