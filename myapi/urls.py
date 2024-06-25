from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapi import views  # Importe corretamente o módulo views



urlpatterns = [
    path('admin/', admin.site.urls),  # Registrar o aplicativo de administração do Django
    path('', views.index, name='index'),  # Rota para a função index 
    path('enviar-animal-perdido/', views.enviar_animal_perdido, name='enviar_animal_perdido'),  
    path('limpar-animais-perdidos/', views.limpar_animais_perdidos, name='limpar_animais_perdidos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
