from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('voltage/', views.receiveESPData, name='receiveESPData_name'),
    path('getVoltage/', views.sendVoltage, name='sendVoltage_name'),
    path('getCurrent/', views.sendCurrent, name='sendCurrent_name'),
]