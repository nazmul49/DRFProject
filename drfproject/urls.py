from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from api import urls
schema_view = get_swagger_view(title='Omis API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(urls)),

    
]