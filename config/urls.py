from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet
from alunos.views import CidadeViewSet
from alunos.views import PessoaViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)
router.register(r'pessoa', PessoaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
