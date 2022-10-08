from django.urls import path
from Api import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework_swagger.views import get_swagger_view


schema_view = get_schema_view(title='NLP TWEET API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

schema_view = get_swagger_view(title='NLP TWEET API')


urlpatterns = [
    
    path('docs', schema_view, name="docs"),
    path('sentiment-analysis', views.sentimentAnlysis, name="sentimentAnlysis"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
