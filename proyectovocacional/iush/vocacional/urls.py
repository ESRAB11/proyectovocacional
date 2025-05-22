from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreguntaViewSet, crear_usuario, listar_usuarios

router = DefaultRouter()
router.register(r'preguntas', PreguntaViewSet, basename='preguntas')

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/', crear_usuario, name='crear_usuario'),
    path('usuarios/lista/', listar_usuarios, name='listar_usuarios'),
]