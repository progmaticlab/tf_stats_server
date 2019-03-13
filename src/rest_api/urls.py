from django.urls import path
from rest_api import views

urlpatterns = [
    path(route='stats', view=views.stats, name="create_stats_record"),
    path(route="version", view=views.api_version, name="api_version")
]
