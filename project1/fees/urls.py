from django.urls import path
from . import views 
urlpatterns = [
    path('feesdj/',views.fees_dj),
    path('feespy/',views.fees_python),
]