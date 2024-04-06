from django.urls import path
from . import views

urlpatterns = [
        path('base/',views.base),
        path('core/',views.home),
        path('cores/',views.about),
]