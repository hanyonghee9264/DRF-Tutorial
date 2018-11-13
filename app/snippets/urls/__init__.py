from django.urls import include, path

from . import django_fbv, drf_fbv, drf_cbv, drf_mixin, drf_generic_cbv

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include(drf_fbv)),
    path('drf-cbv/', include(drf_cbv)),
    path('drf-mixin/', include(drf_mixin)),
    path('drf-generic/', include(drf_generic_cbv)),
]
