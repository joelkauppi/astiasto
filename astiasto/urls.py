from django.urls import path
from .views import views

app_name = 'astiasto'
urlpatterns = [
    path('', views.index, name='index'),
    path('yhteystiedot/', views.about, name='about'),
    path('vuokraa/', views.rent, name='rent'),
    path('vuokraa/valmis/', views.ordersent, name='ordersent'),
    path('vuokrausehdot/', views.terms, name='terms'),
    path('kalenteri/', views.calendar, name='calendar'),
]
