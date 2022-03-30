from django.urls import path
from .views import CalculatorView, result_view

urlpatterns = [
    path('', CalculatorView.as_view(), name='index'),
    path('result/<int:pk>',result_view,name='result')
]
