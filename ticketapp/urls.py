from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('tickets_list/', views.tickets_list, name='tickets_list'),
]
