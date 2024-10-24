from django.urls import path
from . import views

urlpatterns = [
    path('', views.pick_snack, name='pick_snack'),
    path('buy', views.buy, name='buy'),
    path('pay', views.pay, name='pay'),
    path('paid', views.paid, name='paid'),
    path('ask_math', views.ask_math, name='ask_math'),
    path('response', views.response, name='response'),
    path('correct', views.correct, name='correct'),
    path('wrong', views.wrong, name='wrong'),
]