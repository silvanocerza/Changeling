from django.urls import path, include
from django.contrib import admin

{% if cookiecutter.use_django_rest_framework == "y" %}
apipatterns = ([
    path('', include('api.urls')),
], 'api')
{% endif %}
urlpatterns = [
    {% if cookiecutter.add_frontend == "y" %}path('', include('frontend.urls')),{% endif %}
    {% if cookiecutter.use_django_rest_framework == "y" %}path('api/', include(apipatterns, namespace='api')),{% endif %}
    path('admin/', admin.site.urls),
]
