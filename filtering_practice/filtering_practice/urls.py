
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("filter_app/", include('filter_app.urls')),
    path("", views.index),
    path("admin/", admin.site.urls),
]
