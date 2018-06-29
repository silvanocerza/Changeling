from django.conf.urls import url, include
from django.contrib import admin


{% if cookiecutter.use_django_rest_framework == "y" %}
apipatterns = [
    url(r'', include('api.urls')),
]
{% endif %}

urlpatterns = [
{% if cookiecutter.add_frontend == "y" %}
    url(r'', include('frontend.urls')),
{% endif %}
{% if cookiecutter.use_django_rest_framework == "y" %}
    url(r'^api/', include(apipatterns, namespace='api')),
{% endif %}
    url(r'^admin/', admin.site.urls),
]
